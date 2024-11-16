from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, BKnave),
    Or(AKnight, BKnight),
    Implication(BKnight, Not(And(AKnight, BKnave))),
    Implication(BKnave, And(AKnave, BKnave)),
    Implication(AKnave, And(AKnave, BKnight))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, BKnight),
    Or(AKnave, BKnave),
    Or(AKnight, BKnave),
    Or(AKnave, BKnight),

    Implication(AKnight, And(AKnight, BKnight)),
    Implication(AKnave, And(AKnave, BKnight)),

    Implication(BKnight, And(BKnight, AKnave)),
    Implication(BKnave, And(AKnave, BKnave))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    Or(AKnight, BKnight, CKnight),
    Or(AKnave, BKnight, CKnight),
    Or(AKnight, BKnave, CKnight),
    Or(AKnight, BKnight, CKnave),
    Or(AKnight, BKnave, CKnave),
    Or(AKnave, BKnave, CKnave),

    Implication(AKnight, And(AKnight, BKnave, CKnight)),
    Implication(AKnave, And(AKnave, BKnight, CKnave)),

    Implication(BKnight, And(BKnight, CKnave, AKnave)),
    Implication(BKnave, And(BKnave, CKnight, AKnight)),

    Implication(CKnight, And(CKnight, AKnight, BKnave)),
    Implication(CKnave, And(CKnave, AKnave, BKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            found = False  # Flag to check if any truth is found
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
                    found = True
            if not found:  # If no truths were found
                print("    No conclusions could be drawn.")


if __name__ == "__main__":
    main()
