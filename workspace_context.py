import os
import time

def get_workspace_context(base_path=".") -> str:
    """
    Generate a summary of the file system for the current workspace.
    """
    summary = ["Workspace Context:"]
    for root, dirs, files in os.walk(base_path):
        depth = root.replace(base_path, "").count(os.sep)
        indent = "  " * depth
        summary.append(f"{indent}📁 {os.path.basename(root)}/")
        
        for d in dirs:
            dir_path = os.path.join(root, d)
            mtime = time.ctime(os.path.getmtime(dir_path))
            summary.append(f"{indent}  📂 {d}/ (Last Modified: {mtime})")
        
        for f in files:
            file_path = os.path.join(root, f)
            size_kb = os.path.getsize(file_path) / 1024
            mtime = time.ctime(os.path.getmtime(file_path))
            summary.append(f"{indent}  📄 {f} (Size: {size_kb:.1f} KB, Last Modified: {mtime})")

    return "\n".join(summary[:300])  # truncate to stay within token limits
