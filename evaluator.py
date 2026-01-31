from embedding import EmbeddingService

class InterviewEvaluator:
    def __init__(self):
        self.embedding_service = EmbeddingService()

        # Ideal answers (can move to DB later)
        self.questions = {
            "1": {
                "question": "What is a stack data structure?",
                "ideal": (
                    "A stack is a linear data structure that follows the Last In First Out principle. "
                    "Elements are added using push and removed using pop."
                )
            },
            "2": {
                "question": "What is a queue data structure?",
                "ideal": (
                    "A queue is a linear data structure that follows the First In First Out principle. "
                    "Elements are inserted at the rear and removed from the front."
                )
            }
        }

    def score_answer(self, ideal, candidate):
        ideal_vec = self.embedding_service.embed(ideal)
        cand_vec = self.embedding_service.embed(candidate)
        similarity = self.embedding_service.cosine_similarity(ideal_vec, cand_vec)
        return round(similarity * 100, 2)

    def verdict(self, score):
        if score >= 80: return "Excellent"
        if score >= 60: return "Good"
        if score >= 40: return "Average"
        return "Needs Improvement"

    def evaluate(self, answers: dict):
        results = []
        total = 0

        for qid, qdata in self.questions.items():
            candidate_answer = answers.get(qid, "")
            score = self.score_answer(qdata["ideal"], candidate_answer)
            total += score

            results.append({
                "question": qdata["question"],
                "answer": candidate_answer,
                "score": score,
                "verdict": self.verdict(score)
            })

        avg_score = round(total / len(self.questions), 2)

        return {
            "results": results,
            "average_score": avg_score,
            "final_verdict": self.verdict(avg_score)
        }
