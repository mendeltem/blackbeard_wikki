"""Example deck. Each slide: title, speech, and either html or fig + cap (figure file in figures/)."""
SLIDES = [
    dict(title="One audio file per slide", html="<p class='lead'>The slide, its voice and its transcript come from one list.</p><ul><li>Edit a sentence: only that slide is re-spoken</li></ul>",
         speech="This is the first slide. The slide, its voice and its transcript all come from one list."),
    dict(title="Controls", html="<ul><li>Space plays or pauses</li><li>Arrow keys change the slide</li><li>T shows the transcript</li></ul>",
         speech="This is the second slide. Space plays or pauses, the arrow keys change the slide, and the letter T shows the transcript."),
]
