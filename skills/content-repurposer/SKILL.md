---
name: content-repurposer
description: "Take any article URL or text and generate optimized social posts for Twitter/X, LinkedIn, Reddit, and email newsletters. Use when: (1) an article needs sharing across platforms, (2) TechStack.dev blog posts need promotion, (3) repurposing content for social distribution, (4) generating platform-specific copy from long-form. Triggers on: repurpose this article, share on social, turn into tweet thread, post to linkedin, generate social posts, content repurposing, article to twitter."
---

# Content Repurposer

Transform one piece of long-form content into 5+ platform-specific posts.

## Workflow

1. **Fetch the content** (if URL provided)
   ```
   web_fetch(url, maxChars=8000)
   ```
2. **Extract key content**: Identify the main thesis, 3-5 key points, a hook, and a call-to-action
3. **Generate platform posts** using the templates below

## Platform Templates

### Twitter/X Thread (5-7 tweets)
- Tweet 1: Hook — provocative question or bold claim from the article (1-2 sentences)
- Tweets 2-5: Key points, one per tweet, with the most compelling stat or insight first
- Tweet 6: Key takeaway or lesson
- Tweet 7: Link to article + relevant hashtags

**Rules:** 280 char limit per tweet, no hashtags in first 3 tweets, use threading naturally

### LinkedIn Post
- Opening hook: bold statement or surprising stat (first line must stop scrollers)
- Body: 2-3 paragraphs summarizing the article's main argument
- Data/stats: include specific numbers from the article
- CTA: "Link in comments" or direct link
- Tags: 3-5 relevant hashtags at the end

**Rules:** First line = make it compelling, third-person makes it feel less salesy

### Reddit Post (r/... or comment)
- Title: "I analyzed [topic] and found [unexpected insight]" format
- Body: Summary of article + specific examples/data
- Comment style: helpful, not promotional — share value first

### Email Newsletter Snippet
- Subject line: curiosity-driven, under 50 chars
- Preview text: one compelling sentence
- Body: 150-200 words covering the main insight + link

## Reference
See `references/platform-rules.md` for detailed character limits and best practices per platform.
