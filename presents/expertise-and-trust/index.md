---
layout: reveal-provocation
title: "Expertise and Trust in Humanities AI"
---

{::options parse_block_html="true" auto_ids="false" /}

<!-- 01 ------------------------------------------------------------------ -->
<section class="s-title scrim-left"
 data-background-image="images/sandia.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="Title">

Current work
{: .pv-eyebrow}

# Expertise and Trust in Humanities AI
{: .xl}

What AI changes about humanities research, and who has to be trusted for any of it to count.

<div class="foot">

Fred Gibbs
: fredgibbs.net

History
: history.unm.edu

Amaranth
: amaranth.unm.edu


{: .pv-meta}
</div>

<aside class="notes">
**0:00–0:30**

Fifteen minutes. The deck alternates: a claim, then the thing the claim is about. I am going to move fast through a lot of projects, because the argument is in the pattern across them rather than in any one of them.

The through-line: AI moved the cost of doing humanities work, and it moved it in a direction that puts more weight on human judgment, not less — which makes the question of who we trust, and on what basis, the practical problem rather than the philosophical one.
</aside>
</section>

<!-- 02 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Amaranth is a studio, not a service desk">

Amaranth
{: .pv-eyebrow}

## A studio, not a service desk.

---

Amaranth is UNM's digital humanities studio: a room, a printer, a few machines, and students. No dev team, no grant-funded engineering staff. Faculty are asked to bring a **half-formed question** rather than a finished project, and the work gets built in public on infrastructure the authors keep.
{: .full}

<aside class="notes">
**0:30–1:08**

Open here, because every problem in this talk comes out of this room. Cultivating Amaranth has been most of my institutional energy for the last two years, so a word about what it is and what it deliberately isn't.

A service desk takes a finished request and returns a deliverable. That model fails in the humanities, because the interesting decisions are all upstream — what counts as an item, what the metadata should be, what the argument is. By the time the request is well specified, the scholarship has already been done, usually badly.

So we ask for the half-formed question instead, and we sit in the design conversation. Everything in the rest of this talk came out of a conversation like that.
</aside>
</section>

<!-- 03 ------------------------------------------------------------------ -->
<section class="s-plate band-md"
 data-background-image="images/amaranth-home.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="Amaranth, UNM's digital humanities studio">

amaranth.unm.edu
{: .pv-eyebrow}

## Built by undergraduates and one faculty member.

<aside class="notes">
**1:08–1:36**

Hold this number in mind, because the argument at the end depends on it: the site you're looking at, and every project I am about to show you, was made by undergraduates and one faculty member. That was not possible three years ago at this scale, and the reason it is possible now is the subject of the next several slides.
</aside>
</section>

<!-- 04 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="We can already trust AI">

Research
{: .pv-eyebrow .terra}

## We can already trust AI.

---

Do you trust me? That is the real issue. AI is trustworthy in the sense that skilled users know what to expect and that AI output is already consistent (while improving). The question we need to answer is how do we know to trust those who use it?
{: .full}

<aside class="notes">
**1:36–2:18**

Now the problem, and it is not the one the room expects. This is also not a position I arrived with — it is what the studio work kept running into, project after project, until it became the research question.

I am not much worried about whether the model is reliable. Inside a task you have scoped, it is: a skilled user knows what it will do, the output is consistent, and it improves. Treating "can we trust AI" as the open question has eaten a lot of faculty meetings and settled nothing.

The open question is the one on the slide. When I hand you a transcript, a map, a reconstruction, a student essay, you are not evaluating the model. You are evaluating me — whether I knew enough to check it, whether I actually checked, and whether I told you where I stopped. That is a claim about expertise, and we have no established way to warrant it yet.

So: do you trust me? Everything after this slide is the attempt to earn a yes.
</aside>
</section>

<!-- 05 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/sketchbook.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="The AI Sketchbook: research sketches">

AI Sketchbook
{: .pv-eyebrow}

## Field notes, including the failures.

A shared space where colleagues try things and compare notes — fifteen sketches so far, each tagged with whether it was actually tested.
{: .pv-cap}

<aside class="notes">
**2:18–2:48**

This is where the research is actually happening, and it is deliberately unglamorous. Colleagues try something, write down what happened, and tag it. Each entry has a status — tested, untested — because the honest answer is usually "this half worked."

The reason it is a website and not a paper: the useful unit here is a small, dated, local observation, and by the time it is a paper it is out of date and no longer local.

Read the last line of the intro out loud: students should stay alert to "the borrowed, uneven, and sometimes misleading expertise AI seems to offer." Borrowed expertise is the whole problem from the previous slide in four words — and noticing when you are holding some is a skill, which means it can be taught and it can be evidenced.
</aside>
</section>

<!-- 06 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Scale is no longer the obstacle">

Research workflows
{: .pv-eyebrow .terra}

## Scale is no longer the obstacle.

---

Reading across thousands of pages, drafting transcripts for a whole interview collection, describing a few hundred photographs so they can be searched — all of it is now a few weeks of supervised work rather than a funded project. Which means the binding constraint is no longer capacity. It is **judgment**, and we have not built the training for that.
{: .full}

<aside class="notes">
**2:48–3:30**

The first focus: bringing AI into humanities research itself, not just into the classroom.

Be concrete about what changed. It isn't that the machine is smart. It's that three or four specific bottlenecks — transcription, description, normalization of messy archival data, first-pass reading at scale — got cheap enough that a single researcher or a class can now attempt a collection that used to need a grant and a team.

And be equally concrete about what didn't change: every one of those outputs is wrong somewhere, usually in the places that carry the most meaning. So the work didn't disappear; it moved to checking, and checking requires more expertise than producing did.

Next on this list is mapping: georectification, layer alignment and feature extraction are exactly the technical drudgery that keeps spatial analysis out of a humanities course. AI does the lift; the reading stays ours.
</aside>
</section>

<!-- 07 ------------------------------------------------------------------ -->
<section class="s-plate band-md scrim-none"
 data-background-color="#100d0b"
 aria-label="MemoryTour: a design sketch for place-indexed oral history">

<div class="pv-scene" markdown="0">
 <svg viewBox="0 0 1280 720" preserveAspectRatio="xMidYMid slice" role="img" aria-label="A drawn map interface with numbered stops along a walking route and an open recording card">
 <defs>
 <linearGradient id="mt-ground" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0%" stop-color="#15120f"/>
 <stop offset="100%" stop-color="#0d0b09"/>
 </linearGradient>
 </defs>

 <rect x="0" y="0" width="1280" height="720" fill="url(#mt-ground)"/>

 <!-- the street grid: thin blocks, two arterials -->
 <g stroke="#2e2a24" stroke-width="1.5" fill="none">
 <path d="M150 0 L150 720 M330 0 L330 720 M510 0 L510 720 M870 0 L870 720 M1050 0 L1050 720"/>
 <path d="M0 110 L1280 110 M0 250 L1280 250 M0 530 L1280 530 M0 640 L1280 640"/>
 </g>
 <g stroke="#3b352d" stroke-width="4" fill="none">
 <path d="M690 0 L690 720"/>
 <path d="M0 390 L1280 390"/>
 </g>

 <!-- an acequia: the one non-orthogonal thing on the sheet -->
 <path d="M-20 178 C 180 206, 300 300, 470 348 S 820 470, 1010 470 S 1240 512, 1300 560"
 stroke="#3d4a46" stroke-width="5" fill="none" opacity="0.9"/>

 <!-- open ground, then building footprints -->
 <g fill="#1a1f19" opacity="0.85">
 <rect x="176" y="276" width="126" height="92" rx="3"/>
 <rect x="890" y="136" width="140" height="88" rx="3"/>
 </g>
 <g fill="#272319" stroke="#3b352d" stroke-width="1">
 <rect x="176" y="136" width="84" height="88"/>
 <rect x="272" y="136" width="42" height="88"/>
 <rect x="356" y="136" width="130" height="52"/>
 <rect x="356" y="200" width="60" height="24"/>
 <rect x="536" y="136" width="130" height="88"/>
 <rect x="356" y="276" width="70" height="92"/>
 <rect x="440" y="276" width="46" height="46"/>
 <rect x="536" y="276" width="130" height="50"/>
 <rect x="536" y="340" width="82" height="28"/>
 <rect x="716" y="276" width="130" height="92"/>
 <rect x="1076" y="276" width="126" height="92"/>
 <rect x="1076" y="416" width="90" height="94"/>
 <rect x="176" y="416" width="130" height="94"/>
 <rect x="332" y="416" width="60" height="94"/>
 <rect x="416" y="416" width="70" height="60"/>
 <rect x="536" y="416" width="130" height="94"/>
 <rect x="716" y="416" width="92" height="60"/>
 <rect x="828" y="416" width="42" height="94"/>
 <rect x="896" y="416" width="134" height="94"/>
 </g>

 <!-- the walking route. A tour is an order, so the line is part of the claim -->
 <path d="M210 430 L380 430 L380 286 L540 286 L540 188 L664 188 L664 380 L470 380 L470 470"
 stroke="#d4a84b" stroke-width="2" stroke-dasharray="7 7" fill="none" opacity="0.5"/>

 <!-- stops -->
 <g fill="#100d0b" stroke="#d4a84b" stroke-width="2">
 <circle cx="210" cy="430" r="13"/>
 <circle cx="380" cy="286" r="13"/>
 <circle cx="540" cy="188" r="13"/>
 <circle cx="470" cy="470" r="13"/>
 </g>
 <g font-family="JetBrains Mono, monospace" font-size="12" fill="#d4a84b" text-anchor="middle">
 <text x="210" y="435">1</text>
 <text x="380" y="291">2</text>
 <text x="540" y="193">3</text>
 <text x="470" y="475">5</text>
 </g>

 <!-- the stop that is open, drawn larger and filled -->
 <circle cx="664" cy="380" r="19" fill="#d4a84b"/>
 <circle cx="664" cy="380" r="31" fill="none" stroke="#d4a84b" stroke-width="1.5" opacity="0.45"/>
 <circle cx="664" cy="380" r="46" fill="none" stroke="#d4a84b" stroke-width="1" opacity="0.2"/>
 <text x="664" y="385" font-family="JetBrains Mono, monospace" font-size="13" font-weight="700" fill="#100d0b" text-anchor="middle">4</text>

 <!-- where the listener is standing -->
 <circle cx="300" cy="340" r="7" fill="#de8466"/>
 <circle cx="300" cy="340" r="16" fill="none" stroke="#de8466" stroke-width="1.5" opacity="0.4"/>

 <!-- the card for the open stop. It sits high on the sheet so the stripe at
 the bottom of the slide never lands on it. -->
 <g>
 <rect x="716" y="92" width="452" height="212" fill="#100d0b" stroke="#4a4239" stroke-width="1"/>
 <rect x="716" y="92" width="452" height="3" fill="#d4a84b"/>
 <text x="742" y="128" font-family="JetBrains Mono, monospace" font-size="11.5" letter-spacing="2.4" fill="#a89e90">STOP 04 — 00:41 / 12:18</text>
 <text x="742" y="168" font-family="Space Grotesk, sans-serif" font-size="27" font-weight="700" letter-spacing="-0.6" fill="#e8e0d4">Chispas Farm</text>

 <!-- a waveform: the recording is the object, so it gets the space -->
 <g fill="#de8466">
 <rect x="742" y="197" width="3" height="14"/><rect x="750" y="189" width="3" height="30"/>
 <rect x="758" y="181" width="3" height="46"/><rect x="766" y="193" width="3" height="22"/>
 <rect x="774" y="175" width="3" height="58"/><rect x="782" y="187" width="3" height="34"/>
 <rect x="790" y="197" width="3" height="14"/><rect x="798" y="179" width="3" height="50"/>
 <rect x="806" y="191" width="3" height="26"/><rect x="814" y="185" width="3" height="38"/>
 </g>
 <g fill="#6b6157">
 <rect x="822" y="195" width="3" height="18"/><rect x="830" y="187" width="3" height="34"/>
 <rect x="838" y="199" width="3" height="10"/><rect x="846" y="183" width="3" height="42"/>
 <rect x="854" y="193" width="3" height="22"/><rect x="862" y="177" width="3" height="54"/>
 <rect x="870" y="191" width="3" height="26"/><rect x="878" y="197" width="3" height="14"/>
 <rect x="886" y="181" width="3" height="46"/><rect x="894" y="189" width="3" height="30"/>
 <rect x="902" y="195" width="3" height="18"/><rect x="910" y="185" width="3" height="38"/>
 <rect x="918" y="193" width="3" height="22"/><rect x="926" y="179" width="3" height="50"/>
 <rect x="934" y="197" width="3" height="14"/><rect x="942" y="187" width="3" height="34"/>
 <rect x="950" y="191" width="3" height="26"/><rect x="958" y="181" width="3" height="46"/>
 <rect x="966" y="195" width="3" height="18"/><rect x="974" y="189" width="3" height="30"/>
 <rect x="982" y="199" width="3" height="10"/><rect x="990" y="185" width="3" height="38"/>
 <rect x="998" y="193" width="3" height="22"/><rect x="1006" y="177" width="3" height="54"/>
 <rect x="1014" y="197" width="3" height="14"/><rect x="1022" y="187" width="3" height="34"/>
 <rect x="1030" y="191" width="3" height="26"/><rect x="1038" y="195" width="3" height="18"/>
 <rect x="1046" y="183" width="3" height="42"/><rect x="1054" y="197" width="3" height="14"/>
 <rect x="1062" y="189" width="3" height="30"/><rect x="1070" y="193" width="3" height="22"/>
 <rect x="1078" y="197" width="3" height="14"/><rect x="1086" y="187" width="3" height="34"/>
 <rect x="1094" y="195" width="3" height="18"/><rect x="1102" y="191" width="3" height="26"/>
 <rect x="1110" y="197" width="3" height="14"/><rect x="1118" y="193" width="3" height="22"/>
 <rect x="1126" y="199" width="3" height="10"/><rect x="1134" y="196" width="3" height="16"/>
 </g>

 <text x="742" y="256" font-family="Inter, sans-serif" font-size="15.5" fill="#a89e90">“The ditch ran different before they lined it.</text>
 <text x="742" y="278" font-family="Inter, sans-serif" font-size="15.5" fill="#a89e90">You could hear it from here.”</text>
 <text x="1142" y="292" font-family="JetBrains Mono, monospace" font-size="10.5" letter-spacing="1.6" fill="#6b6157" text-anchor="end">DRAFT TRANSCRIPT — UNCHECKED</text>
 </g>
 </svg>

 <span class="chip warn">Design sketch · nothing is built</span>
 </div>

MemoryTour
{: .pv-eyebrow}

## Oral history, indexed by place.

A design sketch drawn for this talk. The transcript is machine-made and marked unchecked, because that is the state it would actually be in.
{: .pv-cap}

<aside class="notes">
**3:30–4:15**

This is the shape of the thing rather than the thing — say that out loud, and say it before anyone has to ask.

What it is for: we have interview collections whose content is overwhelmingly about *places* — a ditch, a field, a building, a corner — and we store them as a list of files named after people. Indexing by place instead means you can stand somewhere and hear who has talked about it.

The reason this is newly possible: draft transcription across a whole collection is now cheap, and you can get first-pass place extraction out of the same pass. The reason it is still hard is on screen: that transcript is unchecked, and machines mangle exactly the words a project like this is about — Spanish, family names, irrigation vocabulary, local place names. So the label stays on until a person has listened.

If the demo is working, switch to it here.
</aside>
</section>

<!-- 08 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Every reconstruction is an argument with the confidence turned up">

Reconstruction
{: .pv-eyebrow .terra}

## Every reconstruction is an argument with the *confidence turned up*.

---

LiDAR and photogrammetry fail visibly: a gap in a point cloud looks like a gap. A generated elevation looks finished whether or not anyone alive knows what was there. **If we build these, the drawing convention has to carry the evidence** — which is a discipline architectural illustration has had for a century and the new tools do not.
{: .full}

<aside class="notes">
**4:15–4:55**

The other half of the research work is historical reconstruction — buildings and landscapes that are gone, in AR and VR.

The appeal is obvious: you can put a body in a space that no longer exists, which no photograph and no scan can do. The danger is equally obvious once you say it plainly. Scanning records what survived. Reconstruction invents what didn't, and it invents it at the same visual confidence as the parts that are documented.

The fix is not technical and it is not new. Reconstruction drawings have always distinguished extant fabric from conjecture with line weight and hatching. We need to carry that convention into the medium, and we need to do it now, while the conventions are still being set.
</aside>
</section>

<!-- 09 ------------------------------------------------------------------ -->
<section class="s-plate band-md scrim-none"
 data-background-color="#100d0b"
 aria-label="A simulated augmented reality reconstruction of the Alvarado Hotel">

<div class="pv-scene" markdown="0">
 <svg viewBox="0 0 1280 720" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Simulated camera view with a wireframe building reconstruction over a street">
 <defs>
 <linearGradient id="ar-sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0%" stop-color="#1b2430"/>
 <stop offset="56%" stop-color="#3a3740"/>
 <stop offset="100%" stop-color="#6b4a36"/>
 </linearGradient>
 <linearGradient id="ar-ground" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0%" stop-color="#241d18"/>
 <stop offset="100%" stop-color="#0c0a08"/>
 </linearGradient>
 </defs>

 <!-- the camera view: sky, the Sandias, the street -->
 <rect x="0" y="0" width="1280" height="455" fill="url(#ar-sky)"/>
 <path d="M0 330 L120 296 L210 318 L330 268 L430 300 L540 254 L660 292 L790 262 L910 300 L1030 268 L1160 296 L1280 276 L1280 455 L0 455 Z"
 fill="#222731" opacity="0.8"/>
 <rect x="0" y="455" width="1280" height="265" fill="url(#ar-ground)"/>
 <path d="M430 455 L860 455 L1180 720 L110 720 Z" fill="#171310" opacity="0.5"/>

 <!-- what is on the site today: the transportation center -->
 <g fill="#2b2620" opacity="0.92">
 <rect x="0" y="369" width="150" height="86"/>
 <rect x="1130" y="385" width="150" height="70"/>
 </g>

 <!-- ================= the reconstruction overlay =================
 Line weight carries the evidence and nothing here is a
 photograph: solid = documented, dashed = inferred from type,
 dotted = invented. The three chips below name each band. -->

 <!-- arcade: nine bays, solid, well documented in photographs -->
 <g stroke="#d4a84b" stroke-width="2" fill="none" opacity="0.96">
 <path d="M200 455 L200 397 A40 40 0 0 1 280 397 L280 455"/>
 <path d="M298 455 L298 397 A40 40 0 0 1 378 397 L378 455"/>
 <path d="M396 455 L396 397 A40 40 0 0 1 476 397 L476 455"/>
 <path d="M493 455 L493 397 A40 40 0 0 1 573 397 L573 455"/>
 <path d="M591 455 L591 397 A40 40 0 0 1 671 397 L671 455"/>
 <path d="M689 455 L689 397 A40 40 0 0 1 769 397 L769 455"/>
 <path d="M787 455 L787 397 A40 40 0 0 1 867 397 L867 455"/>
 <path d="M884 455 L884 397 A40 40 0 0 1 964 397 L964 455"/>
 <path d="M982 455 L982 397 A40 40 0 0 1 1062 397 L1062 455"/>
 <path d="M188 455 L1074 455"/>
 <path d="M188 369 L1074 369"/>
 <path d="M188 361 L1074 361"/>
 </g>

 <!-- second storey: inferred from what Mission Revival hotels did -->
 <g stroke="#de8466" stroke-width="1.8" fill="none" stroke-dasharray="9 6" opacity="0.92">
 <path d="M188 361 L188 275 L1074 275 L1074 361"/>
 <rect x="216" y="297" width="42" height="44"/>
 <rect x="314" y="297" width="42" height="44"/>
 <rect x="412" y="297" width="42" height="44"/>
 <rect x="509" y="297" width="42" height="44"/>
 <rect x="607" y="297" width="42" height="44"/>
 <rect x="705" y="297" width="42" height="44"/>
 <rect x="803" y="297" width="42" height="44"/>
 <rect x="900" y="297" width="42" height="44"/>
 <rect x="998" y="297" width="42" height="44"/>
 </g>

 <!-- roofline, towers, cupola: no surviving source -->
 <g stroke="#a89e90" stroke-width="1.6" fill="none" stroke-dasharray="2.5 5" opacity="0.8">
 <path d="M168 275 L216 231 L1046 231 L1094 275"/>
 <path d="M246 231 L246 165 L376 165 L376 231"/>
 <path d="M246 165 L311 121 L376 165"/>
 <path d="M886 231 L886 165 L1016 165 L1016 231"/>
 <path d="M886 165 L951 121 L1016 165"/>
 <path d="M574 231 L574 187 L688 187 L688 231"/>
 <path d="M574 187 L631 149 L688 187"/>
 </g>

 </svg>

 <span class="chip warn">Simulation · not a working app</span>
 <span class="chip solid pin-ar-arcade">Arcade · photographed</span>
 <span class="chip dashed pin-ar-windows">Windows · inferred</span>
 <span class="chip dotted pin-ar-roof">Roofline · no source</span>
 </div>

Alvarado Hotel · 1902–1970
{: .pv-eyebrow}

## Solid is photographed. Dotted is invented.

Simulated AR view, drawn for this talk. The line weight is the evidence, the way it is on an archaeological site plan.
{: .pv-cap}

<aside class="notes">
**4:55–5:45**

Spend your time here. This is a drawing of a proposal, not a product — I would rather show an honest drawing than a dishonest render.

The building is the Alvarado Hotel: Charles Whittlesey for the Santa Fe Railway, Mission Revival, the largest of the Harvey hotels, demolished in 1970 over citizen protest. Everyone in Albuquerque knows the hole where it was and almost nobody under sixty has stood inside it.

Now point at the line weights. Solid gold is the arcade, which is extensively photographed. Dashed is the second storey, inferred from what buildings of this type did. Dotted is the roofline and the towers, where I would be inventing. The interface shows its own epistemics — and the confidence lives in the drawing convention, not in a disclaimer nobody reads.

Sources: Charles Whittlesey, Santa Fe Railway, Mission Revival, demolition 1970 — Wikipedia, "Alvarado Hotel." Confirm before presenting if any detail is load-bearing.
{: .sources}
</aside>
</section>

<!-- 10 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="The site is the deliverable, not the paper">

Teaching
{: .pv-eyebrow}

## The site is the deliverable. The paper never was.

---

When public scholarship is the default output rather than something translated out of a seminar paper afterwards, the incentives change on day one: students write for readers, cite for strangers, and design for someone arriving by search. **Research nobody can find is research that didn't happen.**
{: .full}

<aside class="notes">
**5:45–6:25**

Second focus: class projects and digital narratives.

The usual arrangement is that a student writes a paper for one reader who is paid to finish it, and then, if the project is lucky, somebody translates it into something public afterwards. That afterwards almost never arrives.

Invert it. Make the public artifact the assignment. The change in student behaviour is immediate and it is not subtle: they start asking who is going to read this, which is the question that makes all the other questions — about evidence, about structure, about what a stranger already knows — suddenly worth asking.

The scale, if anyone wants it: in the first year this supported 14 courses and about 180 students, and nine collaborative class websites went live.
</aside>
</section>

<!-- 11 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/campus-hero.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="UNM Campus Histories">

UNM Campus Histories
{: .pv-eyebrow}

## A campus surveyed by the people who live in it.

A multi-semester project. Each cohort builds on what the last one made, and the categories on the essay index were invented by students who needed to organize their own work.
{: .pv-cap}

<aside class="notes">
**6:25–6:57**

Students write the history of the buildings they walk through every day. It has run across many semesters and it accumulates, which is rare for coursework and is the feature instructors respond to most.

The moment I like best: once the collection got large enough to browse, students needed categories — academic building, classroom building, public art, landscape. Nobody assigned that. Inventing a classification is preservation work whether or not you call it that, and they arrived at it because they had a practical problem.
</aside>
</section>

<!-- 12 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="The knowledge is already in the community">

Community storytelling
{: .pv-eyebrow .terra}

## The knowledge is already in the community.

---

Farmers along the Middle Rio Grande hold knowledge about water, soil, and land use that exists in no document anywhere. Two courses — qualitative methods and local food systems — went and asked. The site is where what they said becomes **citable**.
{: .full}

<aside class="notes">
**6:57–7:37**

Third focus: community storytelling, and the word that matters in it is *authority*.

The default posture of a university project is that the community is the subject of the research. The posture here is that the community is a source of authority in it. Practically that means the farmer's account of how the ditch worked is evidence, held and published under their name, and the students' job is to make it findable and quotable rather than to summarize it into a paper.

It also means cross-course collaboration, which is administratively annoying and pedagogically excellent: two sets of students with different methods training on the same material.
</aside>
</section>

<!-- 13 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/farming.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="Oral Histories of Farming along the Middle Rio Grande">

What actually changed
{: .pv-eyebrow}

## Draft transcripts in days, not months.

Transcription used to be the budget line that killed the project. It is now the cheap part — and the part that needs checking hardest, because machines mangle names, Spanish, and every term specific to a place.
{: .pv-cap}

<aside class="notes">
**7:37–8:09**

Be concrete and be honest here, because this is the clearest case in the talk of the cost moving rather than disappearing.

Draft transcripts for a whole collection in days instead of months is a real change in what is attemptable: an undergraduate class can now take on a collection that used to need a grant. But the drafts are wrong in exactly the places that matter most — proper nouns, Spanish, local place names, irrigation vocabulary.

So the labour did not vanish. It moved toward deciding what a collection means and who gets to say so, which is the part we actually wanted students doing.
</aside>
</section>

<!-- 14 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Not everything belongs in the nearest tool">

Stewardship
{: .pv-eyebrow .terra}

## Not everything belongs in the nearest tool.

---

Community oral histories, Indigenous collections, unpublished archives: the material that most rewards this work is exactly the material you cannot paste into whatever service happens to be open. Before anything is uploaded we ask who has a stake in it, what the permissions actually cover, and which tool fits — including keeping it on a machine in the room. **That conversation is the method, not the paperwork.**
{: .full}

<aside class="notes">
**8:09–8:52**

This is the question I get asked least and should be asked most, so I put it in unprompted.

The uncomfortable fact: the collections where AI would help the most are the ones with the strongest claims against casual processing. A community's oral histories are not a dataset. Somebody trusted a student with them.

So the rule in the studio is that nothing sensitive goes up before a conversation about who has a stake, what the consent actually covered — consent to be interviewed is not consent to be uploaded — and whether the work can be done on a local machine instead. Sometimes the answer is that we do it slower, by hand. That is a legitimate outcome, and saying so out loud is the only thing that makes the rest of the policy credible.
</aside>
</section>

<!-- 15 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/farmer-profiles.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="Farmer profiles, each crediting the narrator, the interviewer and the authors">

Farmer profiles
{: .pv-eyebrow}

## Narrator, interviewer, author — all named.

Every profile credits the farmer, the student who ran the interview, and the students who wrote it up. Attribution is the visible half of stewardship; the rest happens before the recorder goes on.
{: .pv-cap}

<aside class="notes">
**8:52–9:22**

Point at the credit block on each card, because this is the part people miss.

Three names on every entry: the farmer, the student who did the interview, the students who wrote the profile. Nobody here is a data source. The farmer is an author of the record, the students are visible for work that usually disappears into a grade, and anyone citing this knows exactly whose account they are citing.

It costs nothing to build and it changes what the project is.
</aside>
</section>

<!-- 16 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Xanthan: every part of a page has a name">

Infrastructure
{: .pv-eyebrow}

## Every part of a page has a name.

---

All of this runs on Xanthan: plain text files, Jekyll, GitHub Pages — free to host, nothing to renew, and no vendor who can raise the rent or switch it off. Naming the parts is what lets an AI change *one thing* instead of rewriting the site, and what lets a student see exactly what changed. **A project that outlives its funding is a preservation decision taken on day one.**
{: .full}

<aside class="notes">
**9:22–10:05**

This is the piece that makes the rest of the talk reproducible rather than a story about one lucky studio, so give it a moment.

Two claims. First, durability: plain text on open standards means a project outlives its grant cycle and its author's interest. Some of the sites in the gallery you're about to see have not been touched in years and still work.

Second, and this is the one I care about: the framework is built out of named parts. That constraint is what makes AI assistance safe to hand to a nineteen-year-old. You ask for a change to one named block, you get a change to one named block, and you can see it in the diff. The failure mode of AI web work — ask for a tweak, get a plausible rewrite of everything — is designed out at the level of the building blocks rather than patched at the level of the prompt.
</aside>
</section>

<!-- 17 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/xanthan-gallery.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="A gallery of websites built with Xanthan">

xanthan-web.github.io
{: .pv-eyebrow}

## All of it is plain text underneath.

Course archives, oral history collections, digital exhibits, scrolling narratives, mapped directories, annual reports — every one of these is a real site made by UNM students and faculty.
{: .pv-cap}

<aside class="notes">
**10:05–10:35**

A fast slide: the range is the argument. These are not demos. Each one is a working site with an author who can still edit it, and the whole set is one framework and one set of named parts underneath.

If you want the practical version of my research question — where does judgment have to sit — this is my answer in infrastructure form. Put the building blocks where a person can see and name them, and the machine can help with the assembly.
</aside>
</section>

<!-- 18 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="3D pedagogy: put it back in a hand">

3D pedagogy
{: .pv-eyebrow}

## Scan it — then put it back in a hand.

---

We printed five medieval capitals from Scan the World's collection. Set them on a table and the Romanesque-to-Gothic transition stops being a claim in a textbook: it becomes something you see by *turning two objects*. Scanning is the middle of the pipeline, not the end of it.
{: .full}

<aside class="notes">
**10:35–11:12**

A short detour into 3D, because it is the same argument in a different material.

The files are free and public — Scan the World hosts scans from museum collections. Printing five of them costs almost nothing. What you get for that is a comparison a student can make with their hands, and the print quality is limited by the scan in ways that are themselves worth discussing in class.

The point for this talk: a digitized object that stays on a screen is a photograph with extra steps. The pedagogical value shows up when it comes back out into the room.

The partnership version of this: students have been scanning artifacts at UNM's Maxwell Museum and documenting the workflow so the next person can repeat it, and student researchers have taken 3D printing into high school history classrooms. An undocumented digitization is a one-off, not infrastructure.
</aside>
</section>

<!-- 19 ------------------------------------------------------------------ -->
<section class="s-plate band-md heavy"
 data-background-image="images/capitals-poster.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="The Capitals poster from Amaranth's 3D pedagogy work">

Amaranth · 3D pedagogy
{: .pv-eyebrow}

## The objects on a table, with the argument printed beside them.

Capitals poster, Amaranth studio. Five prints from Scan the World, Romanesque to Gothic, each captioned with its date and the museum that holds the original.
{: .pv-cap}

<aside class="notes">
**11:12–11:42**

The poster exists because the objects on their own do not teach. Five lumps of grey filament on a table are five lumps of grey filament until something tells you what to look at.

So the poster is the contextualizing layer: dates, the church or museum each capital came from, and the specific features that mark the shift. It hangs in the studio next to the prints, and the two together are the lesson. The tone is also deliberate — a poster nobody stops at is a poster that failed.
</aside>
</section>

<!-- 20 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Speculative fiction as a classroom exercise">

Speculative fiction
{: .pv-eyebrow .terra}

## Ask it for a place that never existed.

---

The most useful exercise I have found puts all of this together: have a model generate a landscape, a building, a settlement — something plausible and wholly invented — and then argue about it. The image is not the assignment. **The argument is the assignment.**
{: .full}

<aside class="notes">
**11:42–12:25**

Last section, and it combines everything: the research question, the reconstruction problem, and the classroom.

Generative models are very good at speculative fiction, which is a polite name for confident invention. That is normally the thing we warn students about. Here it is the raw material, on purpose, and out in the open where everyone can see it happening.

The move is to generate something that could not be a photograph of anywhere, hand it to a room of people who know the region, and let them take it apart.
</aside>
</section>

<!-- 21 ------------------------------------------------------------------ -->
<section class="s-plate band-lg"
 data-background-image="images/cliff-model.jpg"
 data-background-size="cover"
 data-background-position="center"
 aria-label="An AI-generated model landscape of cliff dwellings">

AI-generated image
{: .pv-eyebrow .terra}

## What here is real? What isn't?

A generated model landscape of cliff dwellings. No site, no survey, no scale. Students are asked which parts they would defend, on what evidence, and what would settle it.
{: .pv-cap}

<aside class="notes">
**12:25–13:30**

Put it up and let the room work on it for a moment before you say anything. Say clearly that it is AI-generated — after the last two slides it would be absurd not to.

Then the questions, in order. What is doing the work of realism here? The contour terrain reads as a survey model, which is a claim about measurement that nothing in this image is entitled to make. Where are the dwellings placed, and is that where they are actually built? What is the construction — is that masonry coursing or is it texture? What is missing that would be there: middens, water, paths, agriculture, any sign of how anyone got in or out?

A student who knows the Southwest will get to "the siting is wrong" fast. Getting them to say *how they know* is the entire pedagogical payload.
</aside>
</section>

<!-- 22 ------------------------------------------------------------------ -->
<section class="s-statement scrim-none" aria-label="Closing: the complaint is the lesson">

The point
{: .pv-eyebrow}

## The complaint is the lesson.

---

"None of this is real" is exactly the response the exercise is built to produce — and usually the first time a student has had to say precisely *why* it isn't, and what evidence would settle it. That is the skill I am trying to teach, and it transfers to every other confident thing a machine hands them.
{: .full}

<div class="cap-row">
Fred Gibbs · fredgibbs.net · amaranth.unm.edu
{: .pv-cap}

Department of History & Amaranth, University of New Mexico
{: .pv-cap}
</div>

<aside class="notes">
**13:30–15:00**

Land it and stop.

The complaint that generative images are fake is correct, and on its own it is inert. It becomes education at the moment you ask the person complaining to be specific — because being specific about why an image is wrong requires knowing what right looks like, and that is domain expertise, and building it is what we are for.

That is the whole argument. The tools got cheap enough that a student can make things that used to take a team. Whether what they make is any good is a question of judgment, and judgment is the thing we still have to teach — which is why the expertise question I opened with is a teaching question, not a technology question.

Leave the rest of the window for questions.
</aside>
</section>
