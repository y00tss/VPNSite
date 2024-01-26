def format_size(size_in_bytes):
    # Function to format the size in a human-readable format
    for unit in ['B', 'KB', 'MB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0