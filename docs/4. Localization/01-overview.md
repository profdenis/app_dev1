# 1. Overview

## What is Localization?

**Localization** (often abbreviated as "l10n" - L + 10 letters + N) is the process of adapting software to make it suitable for different languages, regions, and cultures. It goes beyond simple translation to include cultural adaptation, formatting conventions, and user experience considerations.

### Key Goals of Localization

1. **Language Support**: Translate text content into target languages
2. **Cultural Adaptation**: Adapt colors, images, and layouts to cultural preferences
3. **Regional Formatting**: Handle dates, numbers, currencies according to local conventions
4. **User Experience**: Ensure the interface feels natural to users from different regions
5. **Market Expansion**: Enable software to reach global audiences effectively

### Localization vs Internationalization

- **Internationalization (i18n)**: The process of designing software architecture to support multiple languages and regions
- **Localization (l10n)**: The actual implementation of language and cultural adaptations

Think of internationalization as building the foundation, and localization as decorating the house for specific cultures.

## Core Principles of Localization

### 1. Externalization
All user-visible text should be separated from source code and stored in external files (translation files). This allows translators to work independently without touching the code.

### 2. Unicode Support
Use Unicode (UTF-8) encoding throughout your application to support characters from all languages, including special characters, accents, and non-Latin scripts.

### 3. Context Awareness
Provide context for translators. The word "Open" can mean different things (verb: to open a file, adjective: currently open, noun: an opening).

### 4. Text Expansion Planning
Different languages require different amounts of space. German text can be 30% longer than English, while Chinese might be more compact. Design flexible layouts.

### 5. Right-to-Left (RTL) Support
Some languages (Arabic, Hebrew) read from right to left, requiring interface mirroring.

