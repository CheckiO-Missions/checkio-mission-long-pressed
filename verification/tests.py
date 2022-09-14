"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["alex", "aaleex"],
            "answer": True
        },
        {
            "input": ["welcome to checkio", "weeeelcome to cccheckio"],
            "answer": True
        },
        {
            "input": ["there is an error here", "there is an errorrr hereaa"],
            "answer": False
        },
        {
            "input": ["hi, my name is...", "hi, my name is..."],
            "answer": False
        }
    ],
    "Extra": [
        {
            "input": ["anagram", "anagram"],
            "answer": False
        },
        {
            "input": ["hey, look up", "hey, look up"],
            "answer": False
        },
        {
            "input": ["do you have cool assignments?", "do you have cool assignments?"],
            "answer": False
        },
        {
            "input": ["no, we don't have assignments", "no, we don't have asssignments"],
            "answer": True
        },
        {
            "input": ["hello from usaaaa", "hello from japannnn"],
            "answer": False
        }
    ]
}
