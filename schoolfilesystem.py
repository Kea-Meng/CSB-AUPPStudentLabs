
#Libraries you may need:
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_file(self, file_path, file_type):
        try:
            if file_type == 'csv':
                self.data = pd.read_csv(file_path)
            elif file_type == 'excel':
                self.data = pd.read_excel(file_path)
            elif file_type == 'txt':
                with open(file_path, 'r') as file:
                    self.data = pd.DataFrame(file.readlines())
            else:
                print('Unsupported file type')
                return None
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print('An error occurred while processing the file:', str(e))


    def transfer_data(self, source_file, source_file_type, destination_file, destination_file_type):
        try:
            # Read data from source file
            if source_file_type == 'csv':
                source_data = pd.read_csv(source_file)
            elif source_file_type == 'excel':
                source_data = pd.read_excel(source_file)
            elif source_file_type == 'txt':
                with open(source_file, 'r') as file:
                    source_data = pd.DataFrame(file.readlines())
            else:
                print('Unsupported source file type')
                return

            # Append data to destination file
            if destination_file_type == 'csv':
                destination_data = pd.read_csv(destination_file)
                combined_data = pd.concat([destination_data, source_data])
                combined_data.to_csv(destination_file, index=False)
            elif destination_file_type == 'excel':
                destination_data = pd.read_excel(destination_file)
                combined_data = pd.concat([destination_data, source_data])
                combined_data.to_excel(destination_file, index=False)
            elif destination_file_type == 'txt':
                with open(destination_file, 'a') as file:
                    file.write(source_data.to_string())
            else:
                print('Unsupported destination file type')
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print('An error occurred while transferring the data:', str(e))

    def fetch_web_data(self, url):
        try:
            # Fetch the webpage
            response = urlopen(url)

            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response, 'html.parser')

            # Extract the text from the webpage
            text = soup.get_text()

            return text
        except Exception as e:
            print('An error occurred while fetching web data:', str(e))

    def analyze_content(self):
        try:
            # Check if data is empty
            if self.data.empty:
                print('No data to analyze')
                return None

            student_a_data = self.data[self.data['student'] == 'Student A']
            average_score = self.data['score'].mean()
            top_score = self.data['score'].max()

            sum_math = self.data['Math'].sum()
            sum_science = self.data['Science'].sum()
            sum_english = self.data['English'].sum()
            sums = {'Math': sum_math, 'Science': sum_science, 'English': sum_english}


            print(f'Overall Performance of Student A:\n - Average score: {average_score}\n - Top-performing class: {top_score}\n')
            
            print(f'Sum of scores for each subject:\n - Math: {sum_math}\n - Science: {sum_science}\n - English: {sum_english}\n')

            print(f'Best subject performance: {max(sums)}\nLow subject performance: {min(sums)}\n')

            print(f'Recommandation\nConsider additional support for {min(sums, key=sums.get)} class\n')

        except Exception as e:
            print('An error occurred while analyzing the content:', str(e))

    def generate_summary(self):
        try:
            # # Check if data is empty
            if self.data.empty:
                print('No data to generate summary')
                return None

            # Calculate basic statistics
            summary = self.data.describe().round(2)
            

            print(f"The Summary\n{summary}")

        except Exception as e:
            print('An error occurred while generating the summary:', str(e))


# Analyze content & display result area
school = SchoolAssessmentSystem()
school.process_file("school_management.csv", "csv")
school.transfer_data("school_management.csv", "csv", "school_management.txt", "txt")
school.analyze_content()
school.generate_summary()