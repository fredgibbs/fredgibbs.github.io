# Slide Images — The 1619 Project (Weeks 12.1 and 12.2)

Three image files, all used by `../index.md`. All are public domain or CC BY;
credits are carried in the `<figcaption>`s and should not be stripped. The
folder is about 1.3 MB.

| File | What it is | Source | License |
|---|---|---|---|
| `pyle-landing-negroes-jamestown-1901.jpg` | Howard Pyle, "Landing Negroes at Jamestown from Dutch Man-of-War, 1619," signed and dated 1901. The cold-open slide. 908×938, re-encoded q86, uncropped | Wikimedia Commons, "Howard Pyle (1853-1911) - Landing Negroes at Jamestown from Dutch Man-of-War, 1619 - 1901.jpg" (the file's credit line is a NRC Handelsblad article of 1 January 2020 reproducing it) | Public domain |
| `hannah-jones-abraji-2018.jpg` | Nikole Hannah-Jones speaking into a microphone, Abraji conference, 29 June 2018. The portrait slide. **Cropped** to 1000×1280 from a 1920×1280 download (original 2000×1333); the crop is centered and keeps the face, microphone and hands. q84 | Alice Vergueiro/Abraji (Associação Brasileira de Jornalismo Investigativo), via Wikimedia Commons, "Nikole Hannah-Jones (43277607852).jpg" | **CC BY 2.0**: attribution and "cropped" are in the caption |
| `first-colored-senator-and-representatives-1872.jpg` | Currier & Ives lithograph, 1872: Senator Hiram Revels and Representatives Turner, De Large, Walls, Long, Rainey and Elliott. The image slide that closes part one. 1800×1358 from 5741×4332, q84 | Library of Congress scan with restoration by Adam Cuerden, via Wikimedia Commons, "First Colored Senator and Representatives.jpg" | Public domain |

## Notes

- **The same lithograph is in the essay.** Hannah-Jones's essay prints it at
  the top of p. 17 with the caption "An 1872 portrait of African-Americans
  serving in Congress" (checked against a page image of the Pulitzer Center
  PDF). The deck's caption says where it runs; the picture itself comes from
  Commons, not from the PDF.
- **Pyle's resolution.** The Commons file is 908×938, and `deck-check.sh`
  warned (1.34×) when it was set as a portrait beside its caption. As a
  landscape figure it displays smaller and clears 1.5×. The Library of Congress
  holds the print (LCCN 2005696251; a 977×1536 TIF on Commons) but it was not
  compared against the Commons crop.
- **Portrait choice.** Three Abraji photographs of Hannah-Jones are on Commons
  from the same session. Two were looked at; the one with the microphone and
  direct gaze was chosen over a profile shot.
- **Re-fetch.**

  ```sh
  curl -L -H 'User-Agent: your-name (your-email)' \
    'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
  sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 84
  ```
