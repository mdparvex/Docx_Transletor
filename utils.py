from typing import List, Tuple, Any

def is_equation(element: Any) -> bool:
    """Check if the element contains an equation."""
    omml_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
    return any(child.tag.startswith(omml_ns) for child in element.iter())

def is_image(run: Any) -> bool:
    """Check if the run contains an image."""
    return bool(
        run._element.findall(
            ".//w:drawing",
            {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"},
        )
    )

def preserve_special_elements(paragraph) -> List[Tuple[Any, Any]]:
    """Extract and preserve special elements like images and equations."""
    special_elements = []
    for i, run in enumerate(paragraph.runs):
        if is_image(run) or (hasattr(run._element, 'iter') and is_equation(run._element)):
            # Store the run object and its index
            special_elements.append((i, run._element))
    return special_elements