# Slide Images — The 1619 Project, Part 2 (Week 12.2)

Four image files, all used by `../index.md`. All are public domain or CC BY;
credits are carried in the `<figcaption>`s and should not be stripped. The
folder is about 2.1 MB.

| File | What it is | Source | License |
|---|---|---|---|
| `hannah-jones-abraji-2018.jpg` | Nikole Hannah-Jones at the Abraji conference, 29 June 2018. The portrait slide, so the deck can quote her before anything else. A copy of the file in `../../1619-project/images/` (cropped there to 1000×1280; see that README) | Alice Vergueiro/Abraji, via Wikimedia Commons, "Nikole Hannah-Jones (43277607852).jpg" | **CC BY 2.0**: attribution and "cropped" are in the caption |
| `douglass-warren-c1879.jpg` | Frederick Douglass, studio portrait by George Kendall Warren, about 1879. Part one, after the letter's objections. 1253×1800 from 2089×3000, grayscale, q84, uncropped | U.S. National Archives (NARA 558770), via Wikimedia Commons, "Frederick Douglass (circa 1879).jpg" | Public domain |
| `dunmore-proclamation-1775.jpg` | Lord Dunmore's proclamation, dated November 7, 1775, as printed (the LOC copy is the issue of November 14). Part two, after the Revolution dispute. 1057×1800 from 1880×3200, grayscale, q86, uncropped | Library of Congress, Rare Book and Special Collections (rbpe.1780180b), via Wikimedia Commons, "DunmoresProclamation.jpg" (color-adjusted on Commons; the LOC scan is inverted) | Public domain |
| `du-bois-battey-c1919.jpg` | W. E. B. Du Bois, studio portrait by C. M. Battey. Part two, before the objectivity dispute. 1429×1800 from a 3840×4837 download (original 4620×5820), q84, uncropped | Library of Congress, LCCN 2003681451, via Wikimedia Commons, "W.E.B. (William Edward Burghardt) Du Bois, 1868-1963 LCCN2003681451.jpg" | Public domain |

## Notes

- **The Dunmore quotation is from the image.** The caption quotes "that are able
  and willing to bear Arms" from the broadside itself ("all indented Servants,
  Negroes, or others, (appertaining to Rebels,) free that are able and willing
  to bear Arms, they joining His Majesty's Troops"). "The culmination of the
  slavery dispute" paraphrases Silverstein's reply ("The culmination of this was
  the Dunmore Proclamation").
- **Du Bois's date.** Commons gives 1919; the LOC record itself was not opened.
  The caption says "about 1919."
- **Douglass's caption** ("born enslaved in Maryland... best-known Black
  abolitionist") is general knowledge, not from the readings.
- **No portraits of the five historians, Silverstein, Serwer or Friedersdorf.**
  Serwer is the narrator; the letter's signers are treated as one voice, at the
  author's direction ("we don't need to be as explicit by author"); Commons has
  no photograph of Friedersdorf.
- **Re-fetch.**

  ```sh
  curl -L -H 'User-Agent: your-name (your-email)' \
    'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
  sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 84
  ```
