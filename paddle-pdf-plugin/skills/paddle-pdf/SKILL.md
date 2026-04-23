---
name: paddle-pdf
description: Convert PDF files to Markdown using PaddleOCR API. Use this skill whenever the user mentions PDF conversion, OCR, extracting text from PDFs, converting scanned documents, or needs Markdown output from PDFs. Also trigger for: batch PDF processing (multiple files, concurrent conversion), stdin batch mode, staggered task starts, extracting images from PDFs, RAG data preparation, page selection (specific pages only), resume interrupted conversions, and any request involving PaddleOCR. ALWAYS use this skill for PDF→Markdown workflows - it handles credential setup, large file splitting (80+ pages), output format selection, batch concurrency control, and error recovery automatically.
---

# paddle-pdf CLI Skill

This skill enables converting PDF files to Markdown using the PaddleOCR official API. It handles everything from simple conversions to large batch processing with resume support.

**Supported Models:**
- `paddleocr-vl-1.5` - Document parsing model (default, recommended)
- `paddleocr-vl` - Alternative document parsing model

Both models return the same output format (Markdown + images). Each model has independent quota tracking (20,000 pages/day per model).

## When to Use This Skill

**Trigger this skill when the user:**
- Asks to convert a PDF to Markdown
- Needs to extract text from a PDF using OCR
- Wants to process large PDF files (100+ pages)
- Needs images extracted from a PDF
- Requests JSON metadata with OCR data (for RAG systems)
- Mentions batch processing multiple PDFs
- Wants to convert multiple files concurrently
- Needs to process files from stdin or a file list
- Wants staggered task starts to avoid API overload
- Needs to process specific pages only (--pages)
- Had a conversion interrupted and needs to resume

**Do NOT trigger for:**
- Simple PDF reading (use built-in PDF tools if user ask to not perform with this skill)
- Converting to formats other than Markdown (unless user asks)
- Local OCR processing (this skill uses remote API only)

## Prerequisites

### 1. Check API Credentials

Before any conversion, verify credentials are configured:

```bash
paddle-pdf config show
```

If credentials are missing, guide the user to:

1. **Get credentials:** Visit https://aistudio.baidu.com/paddleocr/task
2. **Configure token:** `paddle-pdf config set-token <token>`
3. **Configure URL for each model:**
   ```bash
   paddle-pdf config set-url <vl15_api_url> --model paddleocr-vl-1.5
   paddle-pdf config set-url <vl_api_url> --model paddleocr-vl
   ```

Alternative: Set environment variables:
```bash
# Required: API token
export PADDLE_OCR_TOKEN=<your_token>

# Required: Model-specific URLs
export PADDLE_OCR_URL_PADDLEOCR_VL_1_5=<vl15_api_url>
export PADDLE_OCR_URL_PADDLEOCR_VL=<vl_api_url>

# Optional: Legacy single URL (for paddleocr-vl-1.5 only)
export PADDLE_OCR_URL=<api_url>

# Optional: Async API URL for large PDFs
export PADDLE_OCR_ASYNC_URL=https://paddleocr.aistudio-app.com/api/v2/ocr/jobs
```

### 2. Verify Environment

```bash
uv run paddle-pdf --version
```

If not installed:
```bash
uv sync --all-extras
```

## Core Workflow

### Step 1: Validate Input

Before running conversion, check:
- PDF file exists at the specified path
- User has API credentials configured
- File size is within limits (≤50MB for PDF, ≤10MB for images)

### Step 2: Choose Conversion Options

Based on user needs, select appropriate options:

| User Need | Options |
|-----------|---------|
| Quick text extraction | `--format minimal` |
| Standard use case | `--format standard` (default) |
| RAG system integration | `--format detailed --json-level full` |
| Large PDF (>80 pages) | `--split-size 80` (auto-splits) |
| No progress output | `--quiet` |
| Custom output location | `-o <output_dir>` |

### Step 3: Run Conversion

```bash
paddle-pdf convert <input.pdf> [options]
```

### Step 4: Verify Output

Check that output directory contains:
- `output.md` - Main Markdown file
- `images/` - Extracted images (if not minimal format)
- `output.json` - Metadata (if not minimal format)

## Available Commands

### convert - Convert PDF to Markdown

```bash
paddle-pdf convert <input.pdf> [options]
```

**Options:**
| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--output` | `-o` | `./output` | Output directory |
| `--model` | `-m` | `paddleocr-vl-1.5` | OCR model: `paddleocr-vl-1.5` or `paddleocr-vl` |
| `--pages` | `-p` | (all) | Page selection: `'1-5,10,15-20'` |
| `--format` | `-f` | `standard` | Output format: minimal/standard/detailed |
| `--json-level` | | `standard` | Metadata detail: minimal/standard/full |
| `--quiet` | `-q` | false | Suppress progress output |
| `--split-size` | | `80` | Pages per chunk for large PDFs |
| `--batch` | | false | Enable stdin batch mode |
| `--jobs` | `-j` | `3` | Concurrent tasks (1-5) for batch mode |
| `--interval` | | `5` | Delay (seconds) between starting each batch task |
| `--token` | | (from config) | API token override |

**Examples:**

```bash
# Basic conversion
paddle-pdf convert document.pdf

# Convert to specific directory
paddle-pdf convert document.pdf -o ./results

# Process specific pages only
paddle-pdf convert document.pdf --pages 1-5,10,15-20

# Full OCR data for RAG
paddle-pdf convert thesis.pdf --format detailed --json-level full -o ./thesis_output

# Quiet mode, large PDF
paddle-pdf convert large.pdf --quiet --split-size 80

# Override credentials
paddle-pdf convert doc.pdf --token my_token --url https://api.example.com

# Batch: multiple files
paddle-pdf convert file1.pdf file2.pdf file3.pdf -o ./output/

# Batch: stdin with custom output
cat files.txt | paddle-pdf convert --batch -o ./output/

# Batch: staggered starts to avoid API overload
paddle-pdf convert *.pdf -o ./output/ --jobs 2 --interval 5
```

### config - Manage Configuration

```bash
# View config status (shows if token/URLs are configured, not actual values)
paddle-pdf config show

# Set API token
paddle-pdf config set-token <token>

# Set API URL for a specific model
paddle-pdf config set-url <url> --model paddleocr-vl-1.5
paddle-pdf config set-url <url> --model paddleocr-vl

# Clear all saved config
paddle-pdf config clear
```

### quota - Check API Quota

```bash
paddle-pdf quota
```

Expected output:
```
Daily Limit: 20,000
Used: 5,000
Remaining: 15,000
```

Note: Each model (paddleocr-vl-1.5, paddleocr-vl) has independent quota tracking.

### resume - Recover Interrupted Jobs

```bash
# List incomplete jobs
paddle-pdf resume list

# Resume specific job
paddle-pdf resume job <job_id>

# Clear all cached jobs
paddle-pdf resume clear
```

## Output Formats

### Minimal (`--format minimal`)
- Single `output.md` file
- Images embedded as Base64 data URIs
- No JSON metadata file
- Best for: Simple text extraction, smallest output

### Standard (`--format standard`, default)
- `output.md` - Markdown with image references
- `images/` folder - Extracted PNG files
- `output.json` - Basic metadata
- Best for: General use, web publishing

### Detailed (`--format detailed`)
- Everything in Standard format
- Additional full OCR data in JSON
- Bounding boxes, confidence scores
- Best for: RAG systems, document analysis

## Output Directory Structure

### Single File Output
```
output/
├── output.md          # Main Markdown content
├── output.json        # Metadata (if not minimal)
└── images/            # Extracted images
    ├── img_000.png
    ├── img_001.png
    └── ...
```

### Batch Output
```
output/
├── file1/             # Subdirectory for each file
│   ├── output.md
│   ├── output.json
│   └── images/
├── file2/
│   ├── output.md
│   └── ...
└── file3/
    └── ...
```

### Failed Tasks Tracking

Failed batch conversions are recorded in `fail_task.json` in the current directory:

```json
{
  "batch_id": "batch_20260413_abc123",
  "summary": {"total": 10, "succeeded": 8, "failed": 2},
  "failed_tasks": [
    {
      "file": "/path/to/failed.pdf",
      "output_dir": "/path/to/output/failed",
      "error_type": "QuotaExceededError",
      "error_msg": "Daily quota exceeded",
      "job_id": "failed_xyz123"
    }
  ]
}
```

Use `paddle-pdf resume job <job_id>` to retry individual failed files.

## JSON Metadata Levels

### Minimal
```json
{
  "source_file": "document.pdf",
  "output_dir": "./output",
  "total_pages": 10,
  "processed_at": "2026-04-09T21:45:00Z",
  "model": "paddleocr-vl-1.5"
}
```

### Standard (default)
```json
{
  "source_file": "document.pdf",
  "output_dir": "./output",
  "total_pages": 10,
  "processed_at": "2026-04-09T21:45:00Z",
  "model": "paddleocr-vl-1.5",
  "images": ["images/img_000.png", "images/img_001.png"],
  "pages": [
    {"page": 1, "char_count": 1234, "images": 2},
    {"page": 2, "char_count": 567, "images": 0}
  ]
}
```

### Full
```json
{
  ...standard fields...,
  "ocr_data": [
    {
      "page": 1,
      "regions": [
        {
          "type": "text",
          "bbox": [10, 20, 100, 50],
          "text": "Extracted text content",
          "confidence": 0.98
        }
      ]
    }
  ]
}
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `ConfigNotFoundError` | No API credentials found | Run `paddle-pdf config set-token` |
| `InvalidTokenError` | Token is invalid (403) | Verify token from PaddleOCR dashboard |
| `QuotaExceededError` | Daily limit reached (429) | Wait until tomorrow or use different token |
| `FileTooLargeError` | File exceeds limits (413) | PDF must be ≤50MB, images ≤10MB |
| `PDFSplitError` | Failed to split PDF | File may be corrupted or password-protected |
| `JobNotFoundError` | Resume job not found | Run `paddle-pdf resume list` to see available jobs |
| `APIError` | Other API failures | Check error message, use `paddle-pdf resume` to continue |
| `ValidationError` | Invalid file path in batch | Check file exists, verify path format |
| `PageSelectionError` | Invalid page spec | Use format: `'1-5,10,15-20'` |

### Batch-Specific Issues

**Simultaneous API uploads causing 401/timeout:**
- Use `--interval 5` (default) to stagger task starts
- First task starts immediately, subsequent tasks wait before acquiring semaphore
- Prevents server overload from concurrent uploads

**Failed tasks in batch:**
- Check `fail_task.json` for error details and job_id
- Use `paddle-pdf resume job <job_id>` to retry individual files
- Failed tasks don't block other tasks from completing

## API Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Daily quota | 20,000 pages/day | Per user, resets daily |
| Max pages per request | 100 pages | CLI auto-splits at 80 pages |
| PDF file size | ≤50MB | Larger files rejected |
| Image file size | ≤10MB | For image inputs |

## Usage Examples

### Example 1: Simple PDF Conversion

**User:** "Convert this PDF to Markdown: ./reports/quarterly_report.pdf"

```bash
paddle-pdf convert ./reports/quarterly_report.pdf
```

### Example 2: Large Thesis for RAG

**User:** "I have a 250-page thesis that I need to convert with full OCR data for my RAG system"

```bash
paddle-pdf convert thesis.pdf --format detailed --json-level full -o ./thesis_output
```

This will:
- Auto-split into 4 chunks (80 + 80 + 80 + 10 pages)
- Process each chunk with progress display
- Merge results with sequential image numbering
- Generate full JSON with bounding boxes and confidence scores

### Example 3: Batch Processing Multiple PDFs

**User:** "I have 20 PDF files in my documents folder to convert"

```bash
# Option 1: Multiple files as arguments (recommended)
paddle-pdf convert ./documents/*.pdf -o ./output/ --jobs 3 --interval 5

# Option 2: Stdin batch mode with file list
cat files.txt | paddle-pdf convert --batch -o ./output/

# Option 3: Custom output per file (stdin format)
echo -e "file1.pdf|output_a/\nfile2.pdf|output_b/" | paddle-pdf convert --batch
```

**Batch features:**
- `--jobs 3`: Process up to 3 files concurrently (max 5)
- `--interval 5`: Stagger task starts by 5 seconds to avoid API overload
- Output creates subdirectories per file: `output/file1/`, `output/file2/`, etc.
- Failed conversions tracked in `fail_task.json` with error details and job_id for retry

### Example 4: Resume Interrupted Conversion

**User:** "My conversion stopped halfway when the internet went down"

```bash
# Find incomplete jobs
paddle-pdf resume list

# Output shows:
#   thesis_20260409_abc123: 2 chunks pending

# Resume the job
paddle-pdf resume job thesis_20260409_abc123
```

The resume feature:
- Preserves completed chunks
- Only processes remaining chunks
- Merges all results after completion
- Automatically cleans up cache when done

## Development Commands

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_cli.py -v

# Type checking
uv run mypy src/

# Format code
uv run ruff format src/

# Lint code
uv run ruff check src/
```

## Troubleshooting

### Common Issues

#### "No API URL configured"

**Problem:** Token is set but URL is missing for the selected model.

**Solution:**
```bash
paddle-pdf config set-url https://your-url.aistudio-app.com/layout-parsing --model paddleocr-vl-1.5
paddle-pdf config set-url https://your-url.aistudio-app.com/layout-parsing --model paddleocr-vl
```

Both token AND model-specific URL must be configured for the CLI to work.

#### "No API credentials found"

**Problem:** Neither token nor URL is configured.

**Solution:**
```bash
paddle-pdf config set-token <your_token>
paddle-pdf config set-url <api_url> --model paddleocr-vl-1.5
paddle-pdf config set-url <api_url> --model paddleocr-vl
```

Or set environment variables:
```bash
export PADDLE_OCR_TOKEN=<your_token>
export PADDLE_OCR_URL_PADDLEOCR_VL_1_5=<vl15_api_url>
export PADDLE_OCR_URL_PADDLEOCR_VL=<vl_api_url>
```

#### "Invalid API token"

**Problem:** Token returned 403 error.

**Solution:**
1. Verify token at https://aistudio.baidu.com/paddleocr/task
2. Check for typos or extra whitespace
3. Re-copy the token fresh from the dashboard

#### "Daily quota exceeded"

**Problem:** Reached 20,000 pages/day limit.

**Solution:**
- Wait until the next day (quota resets daily)
- Use a different API token
- Check quota with `paddle-pdf quota`

#### "File too large"

**Problem:** PDF exceeds 50MB limit.

**Solution:**
- Compress the PDF externally before conversion
- Split the PDF into smaller files manually
- Convert sections separately

#### "PDF splitting failed"

**Problem:** Cannot split the PDF.

**Solution:**
- Check if file is password-protected (decrypt first)
- Verify file is not corrupted (try opening in PDF reader)
- Re-download the file if corrupted

#### "Job not found" during resume

**Problem:** The job ID doesn't exist in cache.

**Solution:**
```bash
# List available jobs
paddle-pdf resume list

# If list is empty, jobs were already completed or cleared
# You'll need to re-run the conversion
```

#### Conversion is slow

**Problem:** Processing takes longer than expected.

**Causes:**
- Large file size (>100 pages)
- Network latency to API
- Complex document with many images

**Solution:**
- Use `--quiet` mode to reduce output noise
- Let it run - large files can take several minutes
- For very large files, conversion happens in chunks automatically

#### "Invalid page spec"

**Problem:** Page specification format is invalid.

**Solution:**
- Use format: `'1-5,10,15-20'` (comma-separated, ranges use hyphen)
- Pages must be ≥ 1 and ≤ total pages
- Example: `--pages 1-5,10,15-20`

### Quick Diagnostic Commands

```bash
# Check credentials status (shows if token/URLs are configured)
paddle-pdf config show

# Check quota
paddle-pdf quota

# List incomplete jobs
paddle-pdf resume list

# Verify installation
uv run paddle-pdf --version
```

## Important Notes

1. **Credentials are required** - Users must obtain API token from PaddleOCR before first use
2. **Model-specific URLs** - Each model (paddleocr-vl-1.5, paddleocr-vl) requires its own URL from the PaddleOCR dashboard
3. **Independent quota** - Each model has separate 20,000 pages/day quota
4. **Large PDFs auto-split** - Files over 80 pages are automatically split and processed in chunks
5. **Resume is automatic** - Interrupted jobs are cached and can be resumed with `paddle-pdf resume`
6. **Output includes images** - Unless using minimal format, extracted images are saved to `images/` folder
7. **Processing time varies** - Allow ~1-2 seconds per page depending on file complexity
8. **Batch concurrency limited** - Max 5 concurrent tasks (`--jobs 5`) to prevent API overload
9. **Staggered starts recommended** - Use default `--interval 5` for batch mode to avoid simultaneous uploads
10. **Failed tasks tracked** - Batch failures saved to `fail_task.json` with retry capability
