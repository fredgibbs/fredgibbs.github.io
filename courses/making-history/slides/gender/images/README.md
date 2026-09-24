# Slide Images — Gender: A Useful Category (6.2)

Seven image files, all used by `../index.md`. Three are public domain; three
are CC BY-SA 3.0, CC BY 3.0 and a Commons public-domain claim, each credited on
its slide; one, `alice-clark-c1922.jpg`, is **fair use** for classroom teaching
— see its row and the Notes.
Credits are carried in the `<figcaption>`s, or in the `.credit` line on a
`.bleed` slide, and should not be stripped.

If you change a filename, update the matching `<img src="…">` or
`data-background-image` in `../index.md`. One file is referenced **twice**:
`berlin-congress-1892.jpg` opens the deck full-bleed, as the puzzle the
session is going to solve, and returns small in the `.with-figure` column of
the part-two discussion slide, so the room is back on screen while the class
argues about what is gendered in it.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `alice-clark-1919-titlepage.jpg` | Title page of Alice Clark, *Working Life of Women in the Seventeenth Century* (London: George Routledge & Sons; New York: E. P. Dutton, 1919), with the University of Toronto library stamp and an ink accession date of 19/12/19. Part one | Internet Archive scan `workinglifeofwom00claruoft`, leaf n6 | Public domain |
| `alice-clark-c1922.jpg` | Alice Clark (1874–1934), studio portrait, c. 1922. Shown beside the title page in a `figure.pair`, part one | LSE Library, via the LSE History blog post "Alice Clark – a suffragist from LSE" (25 July 2018), file `Alice-Cark-c1922.-LSE.jpg` | **Fair use** — see Notes |
| `gerda-lerner-c1981.jpg` | Gerda Lerner (1920–2013), c. 1981, in the University of Wisconsin–Madison Archives (image #S05705). In the narrow column of the sex/gender slide, beside her definition | UW–Madison Archives, via Wikimedia Commons ("UW-Madison history professor Gerda Lerner.jpg") | CC BY 3.0 |
| `bell-hooks.jpg` | bell hooks (1952–2021) speaking. In the narrow column of the "which women" slide, beside her critique of essentialism | Wikimedia Commons ("Bellhooks.jpg"), uploaded by Cmongirl | Public domain as tagged — see Notes |
| `scott-2013-portrait.jpg` | Joan Wallach Scott in front of her bookshelves, 2013; the shelf label "GENDER" is visible behind her. Part two, the portrait slide. **A crop** — see Notes | B. Sutherton, 2013, via Wikimedia Commons ("Joan Wallach Scott and Kristen R. Ghodsee.jpg") | CC BY-SA 3.0 |
| `burke-frontispiece-1790.jpg` | *Frontispiece to Reflections on the French Revolution*, etching, hand-colored: Burke kneeling to a vision of Marie-Antoinette while a cherub touches his head with a firebrand. Publication line: "London Pub.d Novem.r the 2, 1790, by Will.m Holland, N.o 50, Oxford St." Part three | Library of Congress, British Cartoon Prints Collection, ppmsca.05425 (LCCN 2004669854), via Wikimedia Commons | Public domain |
| `berlin-congress-1892.jpg` | Anton von Werner, *Der Kongreß zu Berlin — Schlußsitzung am 13. Juli 1878*, oil on canvas, 127 × 203 cm, 1892: von Werner's later, smaller replica of the mural he painted for the Berlin town hall in 1881. Part three, on its own image slide and again small on the part-three discussion slide | Deutsches Historisches Museum (Lebendiges Museum Online), via Wikimedia Commons ("Congress of Berlin, 13 July 1878, by Anton von Werner.jpg") | Public domain |

Retrieved 2026-09-24; the four Commons files via the `Special:FilePath`
endpoint, the Clark title page from the Internet Archive page-image endpoint.
The folder totals ~5.4 MB, inside the ~10 MB ceiling.

## Notes

**Re-fetch and resize.** All five non-crop files were sourced at 1400–2000px
wide and reduced with the long edge capped at 1800:

```sh
UA='your-name (your-email)'
curl -L -H "User-Agent: $UA" \
  'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 84
```

Quality by file: 86 for `alice-clark-1919-titlepage.jpg` and
`burke-frontispiece-1790.jpg` (fine engraved lines and small type that q78
visibly smears), 88 for `alice-clark-c1922.jpg`, 86 for
`gerda-lerner-c1981.jpg` and `bell-hooks.jpg`, and 82 for
`berlin-congress-1892.jpg`. The Clark title page came from
`https://archive.org/download/workinglifeofwom00claruoft/page/n6_w1600.jpg`.

**One file is a crop.** Nothing has been added to any image; only edges
removed. `scott-2013-portrait.jpg` is the right-hand figure of a two-person
photograph — Scott stands beside Kristen R. Ghodsee, who is cropped out. The
caption on the slide says the frame was cropped. Re-make it with:

```sh
curl -L -H "User-Agent: $UA" \
  'https://upload.wikimedia.org/wikipedia/commons/2/21/Joan_Wallach_Scott_and_Kristen_R._Ghodsee.jpg' -o raw.jpg
sips -c 875 670 --cropOffset 30 600 raw.jpg --out scott-2013-portrait.jpg \
  -s format jpeg -s formatOptions 88
```

It is left at its native 670 × 875 rather than upscaled to the deck's usual
1800px cap: the source is only 1270 × 935, and enlarging a crop of it would
smear a photograph that is already soft. In the `figure.portrait` rail it
renders at close to 1:1.

**`scott-2013-portrait.jpg` is CC BY-SA 3.0 and needs its attribution kept.**
"Photograph by B. Sutherton, 2013, cropped from a larger frame. CC BY-SA 3.0."
is in the `<figcaption>`. Do not strip it, and do not drop the note that it is
a crop — the license requires derivative works to say so.

**`alice-clark-c1922.jpg` is fair use, and this is the reason.** No freely
licensed photograph of Alice Clark exists: she has no image on Wikimedia
Commons or on her Wikipedia article. The copy here is the c. 1922 studio
portrait held by LSE Library, taken from LSE's own history blog, which
captions it as her; a photograph of the same date was published in Margaret C.
Gillett's 1935 pamphlet on Clark. It is a low-resolution copy shown for
identification and commentary in a non-commercial teaching deck, next to the
book she wrote. If LSE Library's own rights statement turns out to allow
reuse, replace this note with the license.

**`bell-hooks.jpg` carries a Commons public-domain tag applied by its
uploader, not by an institution.** That is weaker than the other credits here
and should not be relied on outside classroom use. A CC BY-SA 4.0 alternative
exists — "Bell hooks, October 2014.jpg", by Alex Lozupone — but it is 490 ×
689 and is a crop from a group photograph at the New School; this one is the
better portrait for a small column. Swap if the tag is ever challenged.

**Her name is set lowercase against the theme.** `.cite` is
`text-transform: uppercase`, which renders "bell hooks" as "BELL HOOKS". She
lowercased her name deliberately, so the citation on that slide wraps it in
`<span style="text-transform:none">`. It is the only inline style in the deck.
Don't remove it.

**The von Werner is the 1892 replica, not the 1881 mural.** The mural von
Werner painted for the Festsaal of the Berlin town hall in 1881 is roughly
6.15 × 3.6 m and hangs there still; this canvas is his later 127 × 203 cm
version, which differs in details, including the removal of his own
self-portrait as an onlooker. The filename and the caption both carry 1892
for that reason. The Commons file's own title says "13 July 1878" — that is
the date of the session depicted, not of the painting.
