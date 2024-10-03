import matplotlib.pyplot as plt


class Visualization:
    def __init__(self, df):
        self._df = df

    def visual_of_avg_of_subject(self):
        subjects = list(self._df.keys())
        average_scores = [self._df[subject].mean() for subject in subjects]

        plt.title('Average Score per Subject Across All Semesters')
        plt.bar(subjects, average_scores)
        plt.show()

    def overall_average_score(self):
        overall_average_scores = self._df.mean(axis=1)

        plt.figure(figsize=(10, 6))
        plt.plot(overall_average_scores.index, overall_average_scores.values)

        plt.title('Average Overall Score by Semester')
        plt.show()
