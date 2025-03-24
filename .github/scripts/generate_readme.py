import os

def generate_readme(folder_path, folder_in_repo='', include_subfolders=False):
    readme_lines = ["| File Name | GitHub Link |", "|-----------|--------------|"]

    # Fetch GitHub environment info
    repo_full = os.getenv("GITHUB_REPOSITORY", "")
    branch = os.getenv("GITHUB_REF_NAME", "main")

    if not repo_full:
        print("Missing GITHUB_REPOSITORY environment variable.")
        return

    github_user, repo_name = repo_full.split("/")

    for root, _, files in os.walk(folder_path):
        for file in sorted(files):
            if file == "README.md":
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, folder_path).replace("\\", "/")

            if not include_subfolders and "/" in rel_path:
                continue

            github_path = f"{folder_in_repo}/{rel_path}".strip("/")
            github_url = f"https://github.com/{github_user}/{repo_name}/blob/{branch}/{github_path}"
            readme_lines.append(f"| `{rel_path}` | [View]({github_url}) |")

        if not include_subfolders:
            break

    with open(os.path.join(folder_path, "README.md"), "w") as f:
        f.write("\n".join(readme_lines))

    print("✅ README.md generated at", os.path.join(folder_path, "README.md"))

# --- Run directly if script is called from Actions ---
if __name__ == "__main__":
    generate_readme(
        folder_path="your-folder",           # Change this
        folder_in_repo="your-folder",        # Change this
        include_subfolders=True              # Change as needed
    )
