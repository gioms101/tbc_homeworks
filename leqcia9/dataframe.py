import pandas as pd


class DataFrame:
    def __init__(self):
        self._df = pd.read_csv("student_scores_random_names.csv")
        self._lessons = ["Math", 'Physics', 'Chemistry', 'Biology', 'English']

    def fetch_student_with_fx(self):
        filter1 = (self._df[self._lessons] < 50).any(axis=1)

        return self._df[filter1].drop_duplicates(subset='Student')

    def avg_per_semester_for_subj(self):
        avg_score_per_semester = self._df.groupby(['Semester'])[self._lessons].mean()

        return avg_score_per_semester

    def highest_avg_over_semester_subject(self):
        highest_avg = self._df.groupby(["Student"])[self._lessons].mean().mean(axis=1)

        return highest_avg.idxmax()

    def hardest_subject(self):
        hardest_subject = self._df[self._lessons].mean().idxmin()

        return hardest_subject

    def create_new_df(self, filename):
        new_df = self._df.groupby('Semester')[self._lessons].mean()
        new_df.to_excel(filename)

        return new_df
