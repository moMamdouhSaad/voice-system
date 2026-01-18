# Voice System Architecture (MVP)

## Goal
Generate Arabic speech from text using licensed voice profiles, with full control over pace, silence, and warmth.

## Stack
- Backend: NestJS (API, jobs, orchestration)
- Voice Engine: Python (XTTS, audio processing)
- Queue: BullMQ + Redis
- UI: Simple web interface

## Rules
- NestJS never processes audio directly
- Python handles all TTS and audio
- Voices used are licensed or owned
- Silence and pacing are first-class features

## MVP Scope
- One voice profile
- Text to speech
- Pace & silence control
- Export WAV
