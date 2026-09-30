// Render PDF pages to JPEG with macOS PDFKit.
//
// PDFKit is used instead of poppler (pdftoppm/pdftocairo) because the ASD-STE100
// PDFs reference non-embedded fonts (e.g. Arial-BoldMT); poppler substitutes a
// regular-weight face and bold text is lost in the image. PDFKit resolves the
// PostScript names to the installed macOS fonts.
//
// This tool only renders images. It never extracts text: transcription is done
// by reading the images (see CLAUDE.md).
//
// Build: swiftc -O tools/render_pages.swift -o .work/render_pages
// Usage: .work/render_pages <pdf> <first> <last> <dpi> <outDir>
//        writes <outDir>/p-NNN.jpg (1-based, zero-padded page index)

import AppKit
import PDFKit

let args = CommandLine.arguments
guard args.count == 6,
      let doc = PDFDocument(url: URL(fileURLWithPath: args[1])),
      let first = Int(args[2]), let last = Int(args[3]),
      let dpi = Double(args[4]) else {
  FileHandle.standardError.write("usage: render_pages <pdf> <first> <last> <dpi> <outDir>\n".data(using: .utf8)!)
  exit(1)
}
let outDir = args[5]
let scale = CGFloat(dpi / 72.0)

for i in first...min(last, doc.pageCount) {
  let page = doc.page(at: i - 1)!
  let box = page.bounds(for: .mediaBox)
  let w = Int(box.width * scale), h = Int(box.height * scale)
  let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h,
                             bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
                             isPlanar: false, colorSpaceName: .deviceRGB,
                             bytesPerRow: 0, bitsPerPixel: 0)!
  let cg = NSGraphicsContext(bitmapImageRep: rep)!.cgContext
  cg.setFillColor(NSColor.white.cgColor)
  cg.fill(CGRect(x: 0, y: 0, width: w, height: h))
  cg.scaleBy(x: scale, y: scale)
  page.draw(with: .mediaBox, to: cg)
  let data = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.9])!
  try! data.write(to: URL(fileURLWithPath: String(format: "%@/p-%03d.jpg", outDir, i)))
}
