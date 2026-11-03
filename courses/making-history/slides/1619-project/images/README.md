# Slide Images — The 1619 Project, Part 1 (Week 12.1)

Eight image files; seven are used by `../index.md` (the Pyle slide was cut on 2026-11-03 and its file kept). One, the Magazine cover, is used under fair use; see its row and the Notes. All are public domain or CC BY;
credits are carried in the `<figcaption>`s and should not be stripped. The
folder is about 4 MB. Week 12.2's deck (`../../1619-project-debate/`) keeps
its own copy of the Hannah-Jones portrait.

| File | What it is | Source | License |
|---|---|---|---|
| `pyle-landing-negroes-jamestown-1901.jpg` | Howard Pyle, "Landing Negroes at Jamestown from Dutch Man-of-War, 1619," signed and dated 1901. **Unused since 2026-11-03** (was the slide after the title). 908×938, re-encoded q86, uncropped | Wikimedia Commons, "Howard Pyle (1853-1911) - Landing Negroes at Jamestown from Dutch Man-of-War, 1619 - 1901.jpg" (the file's credit line is a NRC Handelsblad article of 1 January 2020 reproducing it) | Public domain |
| `hannah-jones-abraji-2018.jpg` | Nikole Hannah-Jones speaking into a microphone, Abraji conference, 29 June 2018. The portrait slide. **Cropped** to 1000×1280 from a 1920×1280 download (original 2000×1333); the crop is centered and keeps the face, microphone and hands. q84 | Alice Vergueiro/Abraji (Associação Brasileira de Jornalismo Investigativo), via Wikimedia Commons, "Nikole Hannah-Jones (43277607852).jpg" | **CC BY 2.0**: attribution and "cropped" are in the caption |
| `statue-of-freedom-capitol.jpg` | Thomas Crawford's Statue of Freedom on the Capitol dome, photographed close up. Part one, after "what enslaved people built." 1200×1800 from a 1920×2880 download (original 6031×9046), q82, uncropped | Architect of the Capitol, via Wikimedia Commons, "U.S. Capitol Statue of Freedom.jpg" (from the AOC's Flickr) | Public domain (U.S. government work). The AOC's note on the file asks that it be used for "educational, scholarly, news or personal purposes (not advertising or any other commercial use)"; a course deck is within that |
| `dunlap-broadside-1776.jpg` | The Dunlap broadside, the first printing of the Declaration of Independence, July 1776. Part one, after the Hemings slide. 1484×1800 from a 1920×2328 download (original 4454×5400), q84, uncropped | U.S. National Archives, via Wikimedia Commons, "Dunlap Broadside (Declaration of Independence) (3694394069).jpg" | Public domain |
| `first-colored-senator-and-representatives-1872.jpg` | Currier & Ives lithograph, 1872: Senator Hiram Revels and Representatives Turner, De Large, Walls, Long, Rainey and Elliott. Part two, after Reconstruction. 1800×1358 from 5741×4332, q84 | Library of Congress scan with restoration by Adam Cuerden, via Wikimedia Commons, "First Colored Senator and Representatives.jpg" | Public domain |
| `woodard-and-mother-1946.jpg` | Isaac Woodard and his mother, Eliza, at home, July 1946; she holds a *Daily Worker* whose lower headline reads "Eyes Gouged Out by Cop." Part two, after the Nadir slide. 1800×1394 from a 3840×2975 download (original 9531×7383 scan), q82, uncropped | *Sunday Worker*, 21 July 1946; Tamiment Library, NYU (photos_223_001), via Wikimedia Commons, "Isaac Woodard, Blinded Veteran in His Home. Jul 1946 Slide 1.png" | Public domain (per the Commons file page) |
| `nyt-magazine-cover-2019-08-18.jpg` | Cover of *The New York Times Magazine*, August 18, 2019: the masthead over a gray sky, the sea off Point Comfort, and the issue's opening paragraph in red. After "the essay as a thing." 865×1060, q84, rendered from page 1 of the PDF (vector masthead and type over the photograph) and trimmed of an 11px white page margin | Photograph by Dannielle Bowman for *The New York Times*; the Pulitzer Center's full-issue PDF (Zotero `EBWH6A88/full_issue_of_the_1619_project.pdf`, 100 pp., created 2019-08-12) | **Fair use**; see Notes |
| `press-1862-08-15-colonization-report.jpg` | The unsigned report of Lincoln's August 14, 1862 meeting, as *The Press* (Philadelphia) printed it on August 15, p. 2: the headline and opening paragraphs from column 6, and the bracketed closing line ("[The above is merely given as the substance of the President's remarks.]") from the top of column 7. Part two, after the Lincoln slide. **Two crops joined** with a 40px band in the slide background color; the caption says "two cuts, joined." 795×1413, q86, from the 6600×9300 1-bit page image (300 ppi) | Internet Archive, "The press. - 1862-08-15, 1 edition" (`per_the-press_the-press_1862-08-15_1`; PDF keywords "Reel number 000002822. Sequence number 49," a microfilm scan) | Public domain (1862) |

## Notes

- **The lithograph is in the essay.** Hannah-Jones's essay prints it at the top
  of p. 17 with the caption "An 1872 portrait of African-Americans serving in
  Congress" (checked against a page image of the Pulitzer Center PDF). The
  deck's caption says where it runs; the picture itself comes from Commons.
- **The Woodard photograph is not the essay's.** The essay (p. 19) prints a
  different photograph: Woodard, in uniform and dark glasses, standing with his
  mother, credited to Georgia State University Library. That one is not on
  Commons with a clear license. The Commons photograph shows the same two people
  five months after the beating; the caption does not claim it is the essay's.
- **The Statue of Freedom.** The caption's "raised to the top of the dome in
  1863" rests on the Commons description ("Bronze by Thomas Crawford 1863"); the
  statue was set on the dome on December 2, 1863. "With their unfree hands" is
  the essay's phrase and is quoted as hers.
- **Pyle's resolution.** The Commons file is 908×938, and `deck-check.sh`
  warned (1.34×) when it was set as a portrait beside its caption. As a
  landscape figure it displays smaller and clears 1.5×.
- **The Magazine cover is the one file here not cleared by license.** No free
  copy exists: Commons has only the project's wordmark and the NYT logo, and
  the English Wikipedia article on the project carries no cover (both checked
  2026-11-03). It is used under fair use for in-class teaching: the cover of
  the publication the session studies, shown for identification and comment in
  a non-commercial course deck, from the copy the Pulitzer Center distributes
  free for schools rather than from an agency. It is sized to the slide and no
  larger: the figure displays it at 573×702, so 1060px tall clears the deck's
  1.5× standard (800px drew a 1.14× warning) while staying well under the
  PDF's 1958×2403. `pdfimages` extracts only the photograph; the masthead and
  text are vector, so the slide image is a page render
  (`pdftoppm -f 1 -l 1 -singlefile -scale-to-y 1060 -scale-to-x -1 -png`).
- **The 1862 report.** Library of Congress (Chronicling America) blocks
  scripted access, so the page came from the Internet Archive's copy. Crop
  coordinates, in PDF points on p. 2 (×4.1667 for pixels): opening, x 789–973,
  y 783–1081.5; closing line, x 975–1156, y 395–414. Each crop has a 14px white
  border. The *Press* is the version with quotation marks and "we suffer from
  each other"; the other version ("we suffer on each side," no quotation marks)
  was checked on a page image of the *National Anti-Slavery Standard*, August 23,
  1862, p. 4, which reprints it under the heading "The President Puddering with
  Colonization" and follows it with "Comment by the Tribune." See `../ISSUES.md`.
- **Not used:** a Commons photograph of Jefferson's lap desk (300px, too small)
  and a 1946 news photograph of Woodard with his eyes swollen shut
  ("Isaac-Woodard-1946.jpg", 350×446, too small and harder to show a class).
- **Re-fetch.**

  ```sh
  curl -L -H 'User-Agent: your-name (your-email)' \
    'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
  sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 84
  ```

  The 1862 report:

  ```sh
  curl -L -o press.pdf 'https://archive.org/download/per_the-press_the-press_1862-08-15_1/84026296-84026296-1862-08-15-ed-1.pdf'
  pdfimages -f 2 -l 2 -png press.pdf pg2     # 6600×9300, 300 ppi
  ```
