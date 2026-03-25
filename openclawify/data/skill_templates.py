"""10 built-in OpenClaw skill templates."""

SKILL_TEMPLATES = {
    "webhook-triggered": {
        "name": "Webhook Triggered Skill",
        "description": "Trigger a skill when an HTTP webhook is received. Ideal for CI/CD pipelines, GitHub webhooks, or third-party integrations.",
        "trigger_mode": "webhook",
        "yaml_template": """# {skill_name}

**Trigger:** Webhook received at `/api/hooks/{skill_slug}`

**Description:** {description}

## Trigger Configuration
- Endpoint: `POST /api/hooks/{skill_slug}`
- Auth: `{auth_type}`
- Payload expectation: `{payload_expectation}`

## Workflow Steps
{workflow_steps}

## Tools Used
{tools_list}

## Output
{output_description}
""",
        "variables": ["auth_type", "payload_expectation", "workflow_steps", "tools_list", "output_description"],
    },

    "scheduled-task": {
        "name": "Scheduled Task Skill",
        "description": "Run a skill on a cron schedule. Perfect for daily reports, periodic health checks, or recurring automation.",
        "trigger_mode": "cron",
        "yaml_template": """# {skill_name}

**Trigger:** Scheduled — `{schedule}`

**Description:** {description}

## Schedule
- Cron expression: `{schedule}`
- Timezone: `{timezone}`

## Workflow Steps
{workflow_steps}

## Tools Used
{tools_list}

## Output
{output_description}
""",
        "variables": ["schedule", "timezone", "workflow_steps", "tools_list", "output_description"],
    },

    "content-generator": {
        "name": "Content Generator Skill",
        "description": "Generate structured content (blog posts, newsletters, reports) using AI. Input a topic and get polished output.",
        "trigger_mode": "manual",
        "yaml_template": """# {skill_name}

**Trigger:** Manual — invoked with a topic or keywords

**Description:** {description}

## Input
- Topic/keywords: provided at invocation
- Tone: `{tone}`
- Target audience: `{audience}`
- Word count target: `{word_count}`

## Workflow Steps
1. Research topic using web search
2. Gather relevant sources and data
3. Generate content outline
4. Write full content with proper formatting
5. Apply SEO optimization ({seo_optimization})
6. Return formatted output

## Tools Used
{tools_list}

## Output Format
{output_format}
""",
        "variables": ["tone", "audience", "word_count", "seo_optimization", "tools_list", "output_format"],
    },

    "monitor-alert": {
        "name": "Monitor & Alert Skill",
        "description": "Monitor a service or endpoint and send alerts when conditions are met. Use for uptime monitoring, price alerts, or stock notifications.",
        "trigger_mode": "cron",
        "yaml_template": """# {skill_name}

**Trigger:** Scheduled — `{schedule}`

**Description:** {description}

## Monitor Target
- Target: `{monitor_target}`
- Check type: `{check_type}`
- Threshold: `{threshold}`

## Alert Configuration
- Alert channel: `{alert_channel}`
- Severity levels: `{severity_levels}`
- Cooldown period: `{cooldown}`

## Workflow Steps
1. Fetch current status of `{monitor_target}`
2. Compare against threshold conditions
3. If condition met → format and send alert
4. Log check result

## Tools Used
{tools_list}

## Output
{output_description}
""",
        "variables": ["schedule", "monitor_target", "check_type", "threshold", "alert_channel", "severity_levels", "cooldown", "tools_list", "output_description"],
    },

    "social-poster": {
        "name": "Social Media Poster Skill",
        "description": "Take content (article, blog post, update) and generate optimized posts for social platforms. Supports Twitter/X, LinkedIn, Reddit, and more.",
        "trigger_mode": "manual",
        "yaml_template": """# {skill_name}

**Trigger:** Manual — invoked with content URL or text

**Description:** {description}

## Platforms
{platforms_list}

## Per-Platform Configuration
{platform_config}

## Content Processing
1. Fetch and parse input content
2. Generate {platform_count} platform-specific variants
3. Include relevant hashtags: {hashtags}
4. Apply character limits per platform
5. Return ready-to-post content per channel

## Tools Used
{tools_list}

## Output Format
```json
{{
  "twitter": "{{{{ tweet_content }}}}",
  "linkedin": "{{{{ linkedin_content }}}}",
  "reddit": "{{{{ reddit_content }}}}"
}}
```
""",
        "variables": ["platforms_list", "platform_config", "platform_count", "hashtags", "tools_list"],
    },

    "seo-auditor": {
        "name": "SEO Auditor Skill",
        "description": "Audit a URL for SEO factors and generate an actionable report. Checks title, meta, headings, canonical tags, robots.txt, and sitemap.",
        "trigger_mode": "manual",
        "yaml_template": """# {skill_name}

**Trigger:** Manual — invoked with a URL

**Description:** {description}

## Audit Scope
- Target URL: provided at invocation
- Depth: `{audit_depth}`
- Include competitor analysis: `{competitor_analysis}`

## Checks Performed
1. Title tag (presence, length, keyword)
2. Meta description (presence, length, keyword)
3. Heading hierarchy (H1-H6 structure)
4. Canonical tag configuration
5. Robots.txt accessibility
6. Sitemap.xml presence and quality
7. Open Graph and Twitter Card tags
8. Structured data / schema.org markup
9. Core Web Vitals signals ({core_web_vitals})
10. Content keyword density

## Scoring
- Score 0-100 based on weighted checks
- Grade: A (90+), B (75-89), C (60-74), D (40-59), F (<40)

## Tools Used
{tools_list}

## Output
```json
{{
  "url": "{{{{ url }}}}",
  "score": {{{{ score }}}},
  "grade": "{{{{ grade }}}}",
  "issues": [],
  "recommendations": []
}}
```
""",
        "variables": ["audit_depth", "competitor_analysis", "core_web_vitals", "tools_list"],
    },

    "reddit-researcher": {
        "name": "Reddit Researcher Skill",
        "description": "Scan Reddit for posts matching keywords and summarize findings. Great for market research, pain-point discovery, or community feedback.",
        "trigger_mode": "manual",
        "yaml_template": """# {skill_name}

**Trigger:** Manual — invoked with search keywords

**Description:** {description}

## Search Configuration
- Keywords: provided at invocation
- Subreddits: `{subreddits}` (or auto-detect)
- Sort by: `{sort_by}`
- Time filter: `{time_filter}`
- Max results: `{max_results}`

## Analysis Performed
1. Search Reddit via JSON API and web search fallback
2. Filter posts by relevance score
3. Extract post titles, scores, comment counts, URLs
4. Summarize recurring themes and pain points
5. Identify top contributors and viral patterns
6. Generate actionable insights report

## Output Fields
- **posts_found**: total matching posts
- **top_posts**: ranked list with scores
- **themes**: recurring topics identified
- **sentiment**: overall community sentiment (positive/neutral/negative)
- **opportunities**: potential product or content opportunities

## Tools Used
{tools_list}

## Output Format
```json
{{
  "query": "{{{{ query }}}}",
  "posts_found": {{{{ posts_found }}}},
  "top_posts": [],
  "themes": [],
  "sentiment": "{{{{ sentiment }}}}",
  "opportunities": []
}}
```
""",
        "variables": ["subreddits", "sort_by", "time_filter", "max_results", "tools_list"],
    },

    "uptime-checker": {
        "name": "Uptime Checker Skill",
        "description": "Monitor websites and services for availability. Alert when endpoints go down or respond slowly. Track uptime history over time.",
        "trigger_mode": "cron",
        "yaml_template": """# {skill_name}

**Trigger:** Scheduled — `{schedule}`

**Description:** {description}

## Targets
- Endpoints: `{endpoints}` (comma-separated URLs)
- Check method: `{check_method}` (GET/HEAD)
- Expected status: `{expected_status}`

## Thresholds
- Timeout: `{timeout_seconds}`s
- Slow response threshold: `{slow_threshold}`s
- Retries before alert: `{retries}`

## Alert Channels
{alert_channels}

## Workflow Steps
1. For each endpoint, send HTTP request
2. Record response time and status code
3. On failure: retry {retries} times with backoff
4. If still down → send alert via configured channels
5. Log result to history
6. Generate summary report

## Tools Used
{tools_list}

## Output
```json
{{
  "timestamp": "{{{{ timestamp }}}}",
  "results": [
    {{
      "url": "{{{{ url }}}}",
      "status": "{{{{ status }}}}",
      "response_time_ms": {{{{{ response_time_ms }}}}},
      "uptime_history_pct": {{{{{ uptime_pct }}}}}
    }}
  ]
}}
```
""",
        "variables": ["schedule", "endpoints", "check_method", "expected_status", "timeout_seconds", "slow_threshold", "retries", "alert_channels", "tools_list"],
    },

    "backup-manager": {
        "name": "Backup Manager Skill",
        "description": "Automate file and data backups to local or cloud storage. Configure source paths, destinations, retention policies, and schedule.",
        "trigger_mode": "cron",
        "yaml_template": """# {skill_name}

**Trigger:** Scheduled — `{schedule}`

**Description:** {description}

## Backup Sources
{source_paths}

## Backup Destination
- Type: `{destination_type}`
- Path/URL: `{destination_path}`
- Compression: `{compression}`

## Retention Policy
- Keep last: `{keep_count}` backups
- Delete older: `{delete_older}`
- Verify integrity: `{verify_integrity}`

## Workflow Steps
1. Enumerate files in source paths
2. Create archive ({compression} compression)
3. Generate checksum for integrity verification
4. Transfer to destination
5. Prune old backups per retention policy
6. Send summary report

## Tools Used
{tools_list}

## Output
```json
{{
  "backup_id": "{{{{ backup_id }}}}",
  "files_backed_up": {{{{{ files_count }}}}},
  "total_size_bytes": {{{{{ total_size }}}}},
  "destination": "{{{{ destination }}}}",
  "status": "{{{{ status }}}}"
}}
```
""",
        "variables": ["schedule", "source_paths", "destination_type", "destination_path", "compression", "keep_count", "delete_older", "verify_integrity", "tools_list"],
    },

    "report-generator": {
        "name": "Report Generator Skill",
        "description": "Aggregate data from multiple sources into a formatted report. Supports daily/weekly summaries, analytics dashboards, and executive briefings.",
        "trigger_mode": "scheduled",
        "yaml_template": """# {skill_name}

**Trigger:** Scheduled — `{schedule}`

**Description:** {description}

## Data Sources
{data_sources}

## Report Configuration
- Format: `{report_format}`
- Sections: `{sections}`
- Include charts: `{include_charts}`
- Language/tone: `{tone}`

## Distribution
{distribution}

## Workflow Steps
1. Pull data from each source
2. Aggregate and normalize metrics
3. Calculate trends and comparisons vs prior period
4. Generate sections: {sections}
5. Format output as `{report_format}`
6. Distribute to: {distribution_channels}

## Tools Used
{tools_list}

## Output
```json
{{
  "report_id": "{{{{ report_id }}}}",
  "period": "{{{{ period }}}}",
  "format": "{report_format}",
  "sections": {{sections}},
  "generated_at": "{{{{ generated_at }}}}"
}}
```
""",
        "variables": ["schedule", "data_sources", "report_format", "sections", "include_charts", "tone", "distribution", "distribution_channels", "tools_list"],
    },
}


def get_template(template_name: str) -> dict | None:
    return SKILL_TEMPLATES.get(template_name)


def list_templates() -> list[dict]:
    return [
        {
            "id": key,
            "name": val["name"],
            "description": val["description"],
            "trigger_mode": val["trigger_mode"],
        }
        for key, val in SKILL_TEMPLATES.items()
    ]
