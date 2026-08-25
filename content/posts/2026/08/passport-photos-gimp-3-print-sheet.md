---
title: "Passport photos in GIMP 3: a safer 35 x 45 mm print-sheet guide"
date: "2026-08-25T00:00:00.000Z"
legacy_url: "/2026/08/passport-photos-gimp-3-print-sheet.html"
author: "df"
labels:
  - "GIMP"
  - "passport photo"
  - "photo printing"
  - "Technology"
  - "DIY"
description: "A modern GIMP 3 workflow for arranging permitted 35 x 45 mm ID photos on a 6 x 4 inch print, with clear limits for UK passport applications."
---

<p class="article-lead">GIMP can make a precise 35 x 45 mm photo sheet, but it cannot turn a poor portrait into a compliant passport photo. More importantly, some passport authorities do not permit a digitally cropped or altered image. Check the rules first, then use this guide only where crop and print layout are allowed.</p>

<figure class="article-figure">
  <img src="/assets/images/original/2026/08/passport-photos-gimp-3-print-sheet/passport-gimp-print-sheet.svg" alt="A 35 x 45 millimetre portrait arranged eight times on a 6 x 4 inch print sheet" width="1200" height="675" />
  <figcaption>One correctly sized portrait can fit eight times on a borderless 6 x 4 inch print.</figcaption>
</figure>

> **Rules checked: 25 August 2026.** Passport standards change. The destination authority's current guidance always overrides this tutorial.

## Quick read

- **UK online passport application:** do not crop or retouch the photo in GIMP. GOV.UK says to upload an unaltered image containing your head, shoulders and upper body; its service crops the image.
- **UK paper passport application:** a professional booth or shop is the safer route. The official rules say the 45 x 35 mm print must be professionally produced, unaltered, and not cut down from a larger picture.
- **Other 35 x 45 mm ID or visa photos:** use the GIMP workflow below only if that authority permits digital cropping and local printing.
- **GIMP is useful for layout, not cosmetic correction.** Do not remove blemishes, reshape features, replace the background, add filters, or mirror the face.
- **Measure the final print.** A correct JPEG can still be enlarged, cropped, or given a border by a print kiosk.

## First decide whether GIMP is appropriate

| Application route | Recommendation |
| --- | --- |
| UK passport, online | Skip GIMP. Upload an original, unedited colour JPEG that is at least 600 x 750 pixels and 50KB to 10MB. |
| UK passport, paper form | Use two identical professional 45 mm high x 35 mm wide prints. |
| Other passport, visa, licence, or ID | Use GIMP only if the authority permits it, and follow its exact dimensions, head size, background, file, and print rules. |
| Practice or non-official project | Use this 35 x 45 mm example and adapt it as needed. |

For UK online applications, the official instruction is unusually clear: **do not crop the photo**. If that is your route, stop here and use the [GOV.UK digital photo guide](https://www.gov.uk/photos-for-passports).

## Take the source photo correctly

Most failures begin before GIMP opens. Use a recent, sharp colour photograph with:

- a plain, light-coloured background;
- even natural light and no shadow on the face or wall;
- the camera level with the face, not looking up or down;
- a straight head, open eyes, closed mouth, and neutral expression;
- the full head, both shoulders, and space around the subject;
- no beauty mode, portrait filter, AI enhancement, or digital zoom.

For a UK-style portrait, the person should normally stand about 50 cm from the background and the photographer about 1.5 m away. Take several frames and keep the original files.

<figure class="article-figure">
  <img src="/assets/images/original/2012/09/create-your-own-passport-photo-using/Clipart1-300x195.jpg" alt="A source portrait with room around the head and shoulders before cropping" width="300" height="195" loading="lazy" />
  <figcaption>Start wider than the final portrait. This gives room to position the head without enlarging a small image.</figcaption>
</figure>

## GIMP 3 workflow for an allowed 35 x 45 mm print

The values below create a 300 ppi, 6 x 4 inch JPEG. Each portrait is 413 x 531 pixels, which prints within about 0.05 mm of 35 x 45 mm when the whole sheet is printed at its intended size.

### 1. Work from a copy

Open a duplicate of the original in [GIMP](https://www.gimp.org/downloads/). Save the working file as XCF so the original JPEG remains untouched.

### 2. Crop to a 7:9 portrait ratio

Select the **Crop** tool. In Tool Options:

1. Enable **Fixed Aspect Ratio**.
2. Enter `7:9` for width to height.
3. Draw the crop around the head and upper shoulders.
4. Press Enter to apply it.

If the target uses UK printed-photo proportions, the head from chin to crown should become 29 to 34 mm on the final 45 mm-high print. At this guide's 300 ppi scale, that is roughly 343 to 402 pixels. The crown means the top of the head, not the top of the hair.

<figure class="article-figure">
  <img src="/assets/images/original/2012/09/create-your-own-passport-photo-using/Clipart2_cropped1_1.jpg" alt="Portrait cropped to the 35 by 45 passport photo proportion in GIMP" width="310" height="399" loading="lazy" />
  <figcaption>The crop controls framing only. Do not retouch the face or add a replacement background.</figcaption>
</figure>

### 3. Scale the permitted portrait

Open **Image -> Scale Image** and set:

| Setting | Value |
| --- | ---: |
| Width | 413 px |
| Height | 531 px |
| X resolution | 300 ppi |
| Y resolution | 300 ppi |

Keep the width and height linked. Use a high-quality interpolation option. Save this working portrait as XCF before building the sheet.

### 4. Create the 6 x 4 inch sheet

Choose **File -> New** and create:

| Setting | Value |
| --- | ---: |
| Width | 1800 px |
| Height | 1200 px |
| Resolution | 300 ppi |
| Fill | White |

This is a landscape 6 x 4 inch canvas at 300 ppi.

<figure class="article-figure">
  <img src="/assets/images/original/2012/09/create-your-own-passport-photo-using/gimp_new_image.jpg" alt="The new-image size dialog in an older GIMP version" width="398" height="460" loading="lazy" />
  <figcaption>This legacy screenshot shows the same New Image idea. In GIMP 3, use the 1800 x 1200 values listed above.</figcaption>
</figure>

### 5. Add guides for eight photos

Use **Image -> Guides -> New Guide**. Add guides at these pixel positions:

| Direction | Positions |
| --- | --- |
| Vertical | 74, 487, 900, 1313, 1726 |
| Horizontal | 69, 600, 1131 |

Turn on **View -> Snap to Guides**. The guides form four columns and two rows, leaving a small outer margin for normal lab trimming.

### 6. Duplicate and position the portrait

1. Copy the 413 x 531 portrait.
2. In the sheet, use **Edit -> Paste as -> Paste as Single Layer**.
3. Snap its top-left corner to the first guide intersection at `74, 69`.
4. Duplicate the layer seven times.
5. Move the copies into the remaining guide cells.

The top-left positions are:

```text
74,69     487,69     900,69     1313,69
74,600    487,600    900,600    1313,600
```

<figure class="article-figure">
  <img src="/assets/images/original/2012/09/create-your-own-passport-photo-using/Clipart4_multi-300x201.jpg" alt="Eight copies of a portrait arranged on one print sheet" width="300" height="201" loading="lazy" />
  <figcaption>The older tutorial used a Tile filter. Separate layers and guides are easier to inspect and adjust in GIMP 3.</figcaption>
</figure>

### 7. Export without unnecessary damage

Keep the layered XCF, then choose **File -> Export As** and export a JPEG. A quality setting around 90 to 95 is normally enough; GIMP's documentation notes that values above 95 are generally not useful. Keep the colour profile enabled and do not add sharpening, smoothing, or other effects.

## Print without accidental scaling

At the kiosk or print service:

1. Select a 6 x 4 inch landscape print.
2. Choose borderless or no border.
3. Disable fit, zoom, fill, auto-crop, and automatic enhancement where possible.
4. Order one test print before ordering several copies.
5. Measure the full sheet: it should be 152.4 x 101.6 mm.
6. Measure one portrait: it should be 35 x 45 mm.

If either measurement is wrong, do not compensate by guessing inside GIMP. Find the print service's scaling option or use a service that can print at actual size.

## Video walkthrough

This Diaryfolio video shows the original GIMP workflow. Its interface and pixel recipe are older, but the crop, canvas, duplicate, and export concepts still apply. Use the current values from this article.

<iframe class="article-video" src="https://www.youtube-nocookie.com/embed/PYwyaZg83Xw" title="Making passport photos at home using GIMP" width="760" height="428" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Final check before submission

- Verify the authority's current page, not a remembered size or an old blog post.
- Confirm that digital cropping and home or lab printing are permitted.
- Check physical size, head size, background, pose, lighting, focus, and print quality.
- Keep two identical prints if the application asks for two.
- Do not retouch facial features or rely on GIMP to repair a non-compliant source photo.

For a UK passport, use the official online upload or a professional passport-photo service if there is any doubt. Saving a few pounds is not useful if the application is delayed.

### Sources

| Link | Use |
| --- | --- |
| [GOV.UK: digital passport photos](https://www.gov.uk/photos-for-passports) | Current digital size, format, pose, background, and no-crop rules |
| [GOV.UK: printed passport photos](https://www.gov.uk/photos-for-passports/photo-requirements) | Current 45 x 35 mm print, 29 to 34 mm head, quality, and handling rules |
| [GOV.UK: how to take a digital passport photo](https://www.passport.service.gov.uk/photo/how-to-take-a-photo) | Camera distance, lighting, framing, and expression guidance |
| [GIMP 3 manual: Crop Image](https://docs.gimp.org/3.0/en/gimp-image-crop.html) | Current crop commands |
| [GIMP 3 manual: Print Size](https://docs.gimp.org/3.0/en/gimp-image-print-size.html) | Physical print size and resolution |
| [GIMP 3 manual: Export Image as JPEG](https://docs.gimp.org/3.0/en/file-jpeg-export.html) | JPEG quality and export options |
