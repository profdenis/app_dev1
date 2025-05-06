# 1. Counter Application

## **Exercise: Building a PyQt Counter Application**

### **Part 1: Create the Basic Layout**

- Create a new PyQt application with a main window.
- Add a label to display a number (start with 0).
- Add a button labeled “+” (plus) below the label.
- Arrange the label and button vertically using a layout manager.
- At this stage, do not add any interactivity; just build the static interface.

---

### **Part 2: Add Basic Interactivity**

- Make the “+” button functional: when clicked, it should increase the displayed number by 1.
- Ensure the label updates immediately to show the new value.
- Use appropriate signal and slot mechanisms to connect the button to the logic that updates the counter.

---

### **Part 3: Add More Controls**

- Add a “-” (minus) button to allow decrementing the counter.
- Add a spin box (numeric input) that lets the user choose the amount by which the counter increases or decreases.
- Update the logic so that both the “+” and “-” buttons use the value from the spin box as the step size for
  incrementing or decrementing.
- Place the new controls neatly in the layout.

---

### **Part 4: Create a Settings Window**

- Add a separate settings window that the user can open from the main window (for example, with a “Settings” button).
- In the settings window, include a control (such as a spin box) that allows the user to set the global step size for
  the counter.
- When the step size is changed in the settings window, it should automatically update the step size in the main
  window’s spin box.
- Use custom signals if necessary to communicate changes from the settings window back to the main window.

---

### **Part 5: Add a Reset Feature via the Settings Window**

- In the settings window, add a “Reset” button.
- When the user clicks “Reset,” the counter in the main window should reset to zero.
- Ensure the communication between the settings window and the main window is handled using signals and slots.

---

**Bonus Challenge:**

- Add any additional features you can think of, such as changing the color scheme from the settings window, or
  displaying a message when the counter reaches a certain value.

---

**Instructions:**  
 
- For each part, start from your previous solution and add the new features described. Test your application after
each step to ensure everything works as expected. Focus on organizing your code and using PyQt’s signals and slots
effectively.
- Keep your different versions in different files, for example in the files named `counter1.py`, `counter2.py`,
`counter3.py`, ...

---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.