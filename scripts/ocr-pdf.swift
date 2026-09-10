// ocr-pdf.swift — OCR a scanned PDF to text using macOS Vision.
//
// For course-reading PDFs that have no text layer (pdftotext returns nothing).
// Needs only the Xcode Command Line Tools; no brew packages, no tesseract.
//
//   swiftc -O -o /tmp/ocr-pdf scripts/ocr-pdf.swift
//   /tmp/ocr-pdf path/to/scan.pdf 2 > out.txt
//
// The second argument is a render scale (default 2.0). 2.0 is enough for a
// 300dpi book scan; raise it for small type, at a roughly linear time cost.
// A 16-sheet chapter takes about 20 seconds at scale 2.
//
// Output carries "===== SHEET n =====" markers, one per PDF page. Where the
// scan is two-page spreads, one sheet holds TWO printed pages — see the
// "Cache the text of a scanned reading" rule in courses/SLIDE-STYLE.md for
// why you must then mark printed page numbers before citing from the result.
//
// Vision output is not proofread: verify exact wording against the page image
// before putting anything in quotation marks.

import Foundation
import PDFKit
import Vision

let args = CommandLine.arguments
guard args.count > 1, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: ocr <file.pdf> [scale]\n".data(using:.utf8)!); exit(1)
}
let scale = args.count > 2 ? (Double(args[2]) ?? 2.0) : 2.0

for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let r = page.bounds(for: .mediaBox)
    let w = Int(r.width * scale), h = Int(r.height * scale)
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8,
        bytesPerRow: 0, space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue) else { continue }
    ctx.setFillColor(CGColor(red:1,green:1,blue:1,alpha:1))
    ctx.fill(CGRect(x:0,y:0,width:w,height:h))
    ctx.scaleBy(x: CGFloat(scale), y: CGFloat(scale))
    page.draw(with: .mediaBox, to: ctx)
    guard let cg = ctx.makeImage() else { continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let lines = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    print("\n===== SHEET \(i+1) =====")
    print(lines.joined(separator: "\n"))
}
