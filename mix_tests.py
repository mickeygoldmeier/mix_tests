# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mickey
#
# Created:     28/08/2018
# Copyright:   (c) Mickey 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from random import randint
from fpdf import FPDF
from q_class import Question, Test
import tkinter as tk
import os
import sys
import shutil


def get_test():
    questions = []
    amount = int(input("how many questions in the test: "))
    for i in range(0, amount):
        question = input("qestion number %s: " % str(i))
        amount_of_ansewrs = int(input("how many ansewrs: "))
        ansewrs = []
        for j in range(0, amount_of_ansewrs):
            a1 = input("ansewr number %s: " % str(j))
            ansewrs.append(a1)
        questions.append(Question(question, amount_of_ansewrs, ansewrs))
    return Test(questions)


def print_test(test):
    # make dir
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path + "\\tests"):
        shutil.rmtree(dir_path + "\\tests")
    os.mkdir(dir_path + "\\tests")

    # print tests
    num = int(input("amount of tests: "))
    for num_test in range(1, num + 1):
        test1 = test.mix_test()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(90, 8)
        pdf.set_font("arial", "B", 12.0)
        pdf.cell(ln=1, h=5.0, align="L", w=0, txt="test number %s" % num_test, border=0)
        for j, question in enumerate(test1.question_list):
            pdf.set_font("arial", "B", 11.0)
            pdf.cell(
                ln=1,
                h=5.0,
                align="L",
                w=0,
                txt="%s. " % (j + 1) + question.text,
                border=0,
            )
            for i, ansewr in enumerate(question.ansewrs):
                pdf.cell(
                    ln=1,
                    h=5.0,
                    align="L",
                    w=0,
                    txt="    %s. " % (i + 1) + ansewr,
                    border=0,
                )

        pdf.output(dir_path + "\\tests\\test %s.pdf" % str(num_test), "F")


def write_test(entry_list):
    num_of_questions = int(entry_list[0].get())
    num_of_answers = int(entry_list[1].get())

    question_entry_label_list = []
    for i in range(1, num_of_questions + 1):
        answers_entry_label_list = []
        for j in range(1, num_of_answers + 1):
            answers_entry_label_list.append(
                (creat_label(win, str(j) + "."), creat_text(win))
            )

        question_entry_label_list.append(
            (creat_label(win, str(i) + "."), creat_text(win), answers_entry_label_list)
        )
    plot_test(question_entry_label_list)


def plot_test(q_list):
    widget_list = win.winfo_children()
    for item in widget_list:
        item.grid_forget()
    row = 0
    for i, item in enumerate(q_list):
        item[0].grid(column=0, row=row)
        item[1].config(width=60, height=3)
        item[1].grid(column=2, row=row, columnspan=2)
        for j, ans in enumerate(item[2]):
            row += 1
            ans[0].grid(column=1, row=row)
            ans[1].config(width=60, height=3)
            ans[1].grid(column=2, row=row, columnspan=2)
        row += 1


def creat_label(win, text):
    return tk.Label(win, text=text)


def creat_entry(win):
    return tk.Entry(win)


def creat_button(win, text):
    return tk.Button(win, text=text)


def creat_text(win):
    return tk.Text(win)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    # test = get_test()
    # print_test(test)

    entry_list = []

    num_of_questions_label = creat_label(
        win, "how many questions do you want to have: "
    )
    num_of_questions_entry = creat_entry(win)
    num_of_answers_label = creat_label(win, "how many answers per question: ")
    num_of_answers_entry = creat_entry(win)
    start_test = creat_button(win, "start")

    entry_list.append(num_of_questions_entry)
    entry_list.append(num_of_answers_entry)

    num_of_questions_label.grid(column=0)
    num_of_questions_entry.grid(column=1, row=0)
    num_of_answers_label.grid(column=0)
    num_of_answers_entry.grid(column=1, row=1)
    start_test.grid(column=2)

    start_test.config(command=lambda: write_test(entry_list))

    # start_test.bind("<Button-1>", write_test)


if __name__ == "__main__":
    # win = tk.Tk()
    # win.title("scram")
    # win.geometry("500x500")
    # win.wm_iconbitmap("win_icon.ico")
    # main()
    # win.mainloop()
    a = get_test()
    print_test(a)

