# Slide Images — Making History Jeopardy (review of Weeks 1–7)

Five images used by the clues in `../clues.yml` (the `image: src:` fields),
**all copied from the decks this game reviews**. Four are byte-for-byte copies;
the Luddite print is cropped (see Notes). If one is re-cropped or replaced in
its home deck, copy it here again. If you rename a file, update its `src` in
`../clues.yml`.

Each is a picture clue. Its credit line is hidden on screen until the response
is revealed, because most credits name the answer.

| File | What it is | Copied from | License |
|---|---|---|---|
| `donation-of-constantine.jpg` | The Donation of Constantine, Italian fresco, 13th c., unknown master — clue for Valla ($600, Show your sources) | `../../divine-power-and-statecraft/images/` (Web Gallery of Art) | Public domain |
| `paschal-table-annals.jpg` | Paschal table for AD 950–968, St. Gallen, Stiftsbibliothek, Cod. Sang. 459, p. 21 — clue for the origin of annals ($1000, Show your sources) | `../../divine-power-and-statecraft/images/` (e-codices) | **CC BY-NC 4.0** |
| `lepanto-1571.jpg` | The Battle of Lepanto, 7 October 1571, unknown painter, late 16th c., National Maritime Museum, Greenwich, BHC0261 — clue for Braudel's "surface disturbance" ($800, Zoom out) | `../../annales-longue-duree/images/` | Public domain |
| `leader-of-the-luddites-1812-cropped.jpg` | *The Leader of the Luddites*, hand-colored etching, May 1812, Working Class Movement Library — **cropped**, see Notes — clue for General Ludd ($400, Who counts?) | `../../history-from-below/images/leader-of-the-luddites-1812.jpg` | Public domain |
| `berlin-congress-1892.jpg` | Anton von Werner, *Der Kongreß zu Berlin*, closing session 13 July 1878, painted 1892, Deutsches Historisches Museum — clue for Scott's "high politics" ($1000, Who counts?) | `../../gender/images/` | Public domain |

## Notes

- **The Luddite print is cropped because its engraved title is the answer.**
  The bottom margin reads "THE LEADER OF THE LUDDITES", with "Drawn from Life
  by an Officer" and the publisher's line, and the $400 clue asks for General
  Ludd. The crop keeps the whole picture down to its engraved border and drops
  the margin below it. The on-screen credit says "engraved title cropped".
  Regenerate from the uncropped copy with:

  ```sh
  magick ../../history-from-below/images/leader-of-the-luddites-1812.jpg \
    -crop 1364x1638+0+0 +repage -quality 86 leader-of-the-luddites-1812-cropped.jpg
  ```

- **The paschal table is CC BY-NC 4.0** (e-codices). The credit line is shown
  with the response; the use here is non-commercial teaching, as in the Week 3
  deck that it comes from.

- The other two picture clues were checked for the same problem. The fresco
  has no inscription. The paschal table's column heads read *PASCHAE*, which
  gives the answer only to a student reading Latin at $1000 — left in on
  purpose.
