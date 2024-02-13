from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from  randommaths import RandomMathsProblems
from prettytable import PrettyTable
from fpdf import FPDF
from subprocess import Popen
import datetime

# Define a custom class for the app
class MathProblems(App):
    # Build the user interface
    def build(self):
        
        self.cols=5
        #self.digits=3
        # Create a box layout to arrange the widgets
        layout = GridLayout(cols=2,padding=10)
        # Create three text inputs for numbers
        self.input_digits = TextInput(input_filter="int",text='3', multiline=False)
        self.sums = TextInput(input_filter="int",text='5', multiline=False)
        self.subs = TextInput(input_filter="int",text='5', multiline=False)
        self.mults = TextInput(input_filter="int",text='5', multiline=False)
        Window.size = (300, 160)
        # Add the text inputs to the layout
        layout.add_widget(Label(text="Number of Digits: "))
        layout.add_widget(self.input_digits)
        layout.add_widget(Label(text="Additions: "))
        layout.add_widget(self.sums)
        layout.add_widget(Label(text="Subtractions: "))
        layout.add_widget(self.subs)
        layout.add_widget(Label(text="Multiplications: "))
        layout.add_widget(self.mults)
        # Create a label to display the result
        self.result = Label(text="Result: ")
        # Add the label to the layout
        
        # Create a button to calculate the sum of the numbers
        button = Button(text="Generate")
        # Bind the button to a callback function
        button.bind(on_press=self.logic)
        # Add the button to the layout
        layout.add_widget(button)
        #layout.add_widget(self.result)
        # Return the layout as the root widget
        return layout
    

    def generate_problems(self):
        self.problist=[]
        self.digits=int(self.input_digits.text)
        question=RandomMathsProblems(self.digits)
        # generate the problems
        for _ in range(int(self.sums.text)):
            self.problist.append(question.summation())
        for _ in range(int(self.subs.text)) :
            self.problist.append(question.subtraction())
        for _ in range(int(self.mults.text)) :
            self.problist.append(question.product()) 

    # Define a callback function for the logic
    def logic(self, instance):
        self.generate_problems()
        self.make_report()
        self.write_report_to_file()
        self.open_file_to_user()

    def make_report(self):
        
        blank_row=[]
        divider_row=[]
        header_row=[]
        under_row=[]
        for i in range(self.cols):
            header_row.append('Col'+str(i+1))
            blank_row.append(' '*10)
            divider_row.append('¯'*10)
            under_row.append('_'*10)

        self.report=PrettyTable(border=False, header=False, padding_width=2)
        #self.report.border=False
        self.report.align = "r" #align right all columns
        self.report.field_names=header_row
        i=0

        problen=len(self.problist)
        while i < problen:
            top_row=[]
            bottom_row=[]
            for col in range(self.cols):
                if i+col <problen:
                    top_row.append(f'Q{i+col+1:<4}{self.problist[i+col][0]:>6}')
                    bottom_row.append(f'{self.problist[i+col][3]:<2}{self.problist[i+col][1]:>6}')


            while len(top_row)<self.cols:
                top_row.append('')
            while len(bottom_row)<self.cols:
                    bottom_row.append('')
            

            self.report.add_row(top_row)
            self.report.add_row(bottom_row)
            self.report.add_row(divider_row)
            self.report.add_row(blank_row)
            self.report.add_row(under_row)
            
            i += self.cols

        
        answers=['Answers:-']
        for i ,(_,_,result,_) in enumerate(self.problist):
            answers.append(f'{i+1}:{result}')


        self.answer_key = ' '.join(str(x) for x in answers )
        

    def write_report_to_file(self):
        # nl='\n'
        # with open('sums.txt', 'w') as f:
        #     f.write(self.answer_key+nl)
        #     f.write(str(self.report))
        now = str(datetime.datetime.now())
        ts="".join(c for c in now if c.isalnum())
        self.op_file_name=f'MathProblems{ts}.pdf'
       

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Courier', '', 12)
        pdf.multi_cell(0, 5, str(self.answer_key), 0)
        pdf.multi_cell(0, 3, '\n'*2, 0)
        pdf.multi_cell(0, 3, str(self.report), 0, align= 'C')
        pdf.output(self.op_file_name, 'F')


        # Update the result label
       # self.result.text = f"Problems generated in sums.txt"

    def open_file_to_user(self):
        subproc = Popen(f'start {self.op_file_name}',shell=True)
        subproc.wait()

# Run the app
if __name__ == "__main__":
    MathProblems().run()
