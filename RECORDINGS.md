# Creating voice-recordings

This guide documents the steps taken to produce voice recordings.

## Recording

First record from a good source, used a Sony voice recorder and the quality was acceptable. Sound format to use is 16-bit PCM (that is uncompressed audio). Preferrably do not record to MP3 or other compressed format.

Second while recording, leave a few seconds of space before and after the recording. This space is both used to ensure that you can easily cut the recording in snippets later, but also used to measure noise level for Audacity so that noise can be automatically removed.

## Editing recordings: Audacity

Audacity is a free tool that allows editing of recordings. It can be used to cut the recordings into pieces, as well as to perform effects such as slowing down recordings as well as de-noising.

De-nosiing is especially important and you can use the few seconds of empty recording at the beginning and end of each recording you made to identify noise and automatically remove via Audacity.

When using Audacity, save the results as WAV/Uncompressed PCM format.

## Normalize volume

Likely your recordings will have quite varying volumes. A way to normalize across a bunch of recordings is to the use "normalize-audio" package with the "mix" mode.
```
normalize-audio -m *.wav
```

## Transcoding

Use sox to transcode your wav files into a format that Asterisk will understand:
```
for a in *.wav; do sox "$a"  -r 8k -c 1 -e gsm "`echo $a|sed -e s/wav//`gsm"; done
```

## Done

Now the voice recording files should be ready for use with Asterisk.
