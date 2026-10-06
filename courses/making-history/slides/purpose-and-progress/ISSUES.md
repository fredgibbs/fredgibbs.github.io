# Issues — purpose-and-progress

**What this deck is.** Session 8.1 as seven pictures and two questions. It
covers the same ground as `../what-are-we-talking-about/`, which stays in the
repo as the written record and the handout for anyone who misses class. Present
from this one; send them to that one. If 8.1's prompts change on
`../../schedule.md`, both decks need the edit.

**It breaks two image rules on purpose.** `../../SLIDE-STYLE.md` says "One image
per slide. A second image is a second slide," and allows `figure.pair` only
"after each has had its own slide, and only for a minor comparative point."
Four of the seven slides here are pairs carrying the whole point. The exception
is now written into the guide ("Discussion decks built on image pairs"); this
deck is its worked example. Don't re-raise it.

**No `.takehome` on any picture slide.** Deliberate, and the reason the format
was chosen: a takeaway line closes the question the slide exists to open. The
only two takehomes are on the two discussion slides, which is the one-epigram-
per-part budget the guide asks for. If a later pass adds crux lines under the
pictures, it has undone the deck.

**Every image is new to the course.** No portrait of anyone they have read, no
plate from an assigned text. Students have to apply Carr, Ranke, Marx,
Thompson, Scott and Ginzburg rather than recognise them. That is also the risk:
a room that has not done the reading has nothing to say, and the deck gives
them no text to fall back on. Credits and licenses are in `images/README.md`.

**Three claims on slides that are not from a reading, and where they come from.**
Each is stated on the slide and should survive a student checking it.

- *Blue Marble.* The slide says it "is conventionally printed the other way up
  from how it was taken." The usual account is that AS17-148-22727 came back
  with the South Pole uppermost and is circulated rotated. The slide is
  deliberately phrased as a claim about printing convention, not about NASA's
  intent — don't sharpen it into "NASA flipped it" without a citation.
- *Knossos.* The "Saffron Gatherer" was restored as a human boy and later
  re-identified as a monkey; the surviving fragments include a tail, which the
  Commons file description itself notes. Evans's restorer was Émile Gilliéron.
- *Firdos Square.* "The plaza is nearly empty and the frame is tight" is
  visible in the image and is the standard account of the 9 April 2003 event.
  The slide asks what the photograph is a source for; it does not assert the
  toppling was staged, and shouldn't.

**The Carlisle slide needs saying out loud, not just showing.** Tom Torlino's
before-and-after was made by the school as promotional proof of its own
success, and the deck's question turns on that. Name Carlisle's purpose when it
goes up; a slide of this image with no framing does the school's work for it.
This is a UNM course and the subject is close to home for some of the room.

**The `.provoke` form is new CSS.** `section.image-slide.provoke` is documented
in the header comment of `/assets/css/reveal-image-slide.css`. Two things went
wrong building it and are worth not repeating: the figure must keep its base
`height: 100%` (holding it to a percentage starves the pictures, because the
question and credit are measured inside the figure), and a single landscape
image needs `flex: 1 1 auto; min-height: 0` or it keeps its natural height and
pushes the question off the bottom.

**Rendering checked 2026-10-03.** All eleven slides stepped through headless at
960x700 with fragments forced visible; nothing clips.
`scripts/slide-words.py` passes.

**The schedule does not link this deck.** Add a slides line under 8.1 in
`../../schedule.md` when it is ready to go out.


**Closing slide corrected, 2026-10-06.** It shared the 8.1 text deck's line
"Hobsbawm and Anderson argue they were invented, deliberately," which misstates
Anderson (*Imagined Communities*, pp. 4, 6: nations as imagined, not
fabricated). Both decks now carry the same corrected closing; keep them
identical.
