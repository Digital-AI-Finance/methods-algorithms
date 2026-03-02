# Learnings

## Chart Width Updates in LaTeX

- When encountering file locking issues with Edit tool on Windows, use a Python script via Bash as workaround
- Successfully updated 8 chart widths in L01_deepdive.tex:
  - Most charts: 0.65\textwidth for better visibility
  - 3D plot (02_multiple_regression_3d): 0.55\textwidth to preserve aspect ratio
  - Decision flowchart: 0.65\textwidth (updated from 0.50\textwidth)
- Regex pattern for LaTeX width replacement: `\includegraphics\[width=[\d.]+\textwidth\]{filename}`

