# assets/face-refs/ — your face, for AI thumbnails and carousel covers (optional)

Read by two skills: `thumbnail-generator` (every generation, as the identity anchor) and
`carousel-generator` when a manifest sets `"face_refs": true` on the cover. Both pass every image
here to Higgsfield as `--image` references so the render looks like you.

Drop **4-8 photos of your own face** here: varied angles, expressions and lighting, well lit,
PNG/JPG/JPEG/WEBP. Nothing else in the folder (more than 8 can exceed the model's per-run image
cap). If it's empty, thumbnails refuse to run with `face_refs: true` (before spending anything) and
carousel covers generate without a person.
