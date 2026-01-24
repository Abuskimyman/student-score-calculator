def calculate_student_score(*scores, **options):

    #  Solve for Weight
    weight = options.get("weight", 1.0)
    #  Solve for Bonus
    bonus = options.get("bonus", 0)
    #  Solve for Passmark
    pass_mark = options.get("pass_mark", 50)

    if not scores:
        raise ValueError("At least one score must be provided")

    # Solve for total
    total = sum(scores)

    # Solve for average
    average = total / len(scores)

    # Solve for weight
    weighted_score = average * weight

    # Solve for final score
    final_score = weighted_score + bonus

    # Solve for status of the score
    status = "PASS" if final_score >= pass_mark else "FAIL"

    return {
        "scores": scores,
        "average": round(average, 2),
        "weight": weight,
        "bonus": bonus,
        "final_score": round(final_score, 2),
        "status": status
    }



# Main 

if __name__ == "__main__":

    # Default Scores stored in a list (or tuple)
    student_scores = [78, 85, 90, 88]

    # Configuration stored in a dictionary
    config_options = {
        "weight": 1.1,
        "bonus": 5,
        "pass_mark": 50
    }

    # Function call using unpacking
    report = calculate_student_score(*student_scores, **config_options)

    # Display report
    print("📊 STUDENT SCORE REPORT")
    print("-" * 30)
    print(f"Scores: {report['scores']}")
    print(f"Average Score: {report['average']}")
    print(f"Weight Applied: {report['weight']}")
    print(f"Bonus Points: {report['bonus']}")
    print(f"Final Score: {report['final_score']}")
    print(f"Status: {report['status']}")







