# franklin
The FRANKLIN (FRANK Library of Ideal Narratives) dataset is inspired by the functionality of the FRANK question answering system.

Questions are paired with template-based, natural language, step-by-step decompositions modelled on how FRANK would nominally decompose a problem using formal deductive reasoning.
Four question templates make up the dataset, aiming to represent a variety of meta- and object-level reasoning processes.

Each item in `franklin.json` has the following signature:

```python
{
    "template_id": "str", # UUID 4
    "question_id": "str", # One of A, B, C, D
    "question": "str", # Natural language question
    "explanation": [
        {
            "step": "int", # Step number
            "label": "str", # Label: "meta" or "object"
            "explanation": "str" # Natural language description of step
        }
    ]
}
```
