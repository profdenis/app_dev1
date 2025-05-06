# 2. Layouts Overview

PyQt6 provides several layout managers that automatically arrange widgets within windows, ensuring your GUI adapts well
to resizing and different screen sizes. Here’s an overview of the main layouts available:

## 1. QVBoxLayout

- Arranges widgets vertically, from top to bottom.
- Each widget is placed below the previous one.
- Commonly used for stacking elements in a column.
- Example: A settings panel with labels and input fields stacked vertically[1][2][5][6].

## 2. QHBoxLayout

- Arranges widgets horizontally, from left to right.
- Each widget is placed to the right of the previous one.
- Useful for toolbars, button rows, or any horizontal grouping[1][2][3][5][6].

## 3. QGridLayout

- Arranges widgets in a two-dimensional grid (rows and columns).
- Widgets can span multiple rows or columns.
- Ideal for forms, calculators, or any layout requiring tabular alignment[1][2][5][6].

## 4. QFormLayout

- Specifically designed for forms: pairs labels and fields in two columns.
- Left column: labels; right column: input widgets (e.g., text fields, combo boxes).
- Simpler and more readable than QGridLayout when you only need two columns[4][6][7].

## 5. QStackedLayout

- Stacks widgets on top of each other; only one widget is visible at a time.
- Useful for implementing tabbed interfaces or wizards where you switch between different views[1].

## 6. QSplitter

- Not a layout, but a container widget that arranges child widgets horizontally or vertically with adjustable dividers.
- Allows the user to resize panels interactively[4].

---

## Summary Table

| Layout         | Arrangement                     | Typical Use Case                        |
|----------------|---------------------------------|-----------------------------------------|
| QVBoxLayout    | Vertical (top-down)             | Stacked widgets, forms, settings panels |
| QHBoxLayout    | Horizontal (left-right)         | Toolbars, button rows                   |
| QGridLayout    | Grid (rows/columns)             | Calculators, complex forms              |
| QFormLayout    | Label-field pairs               | Data entry forms                        |
| QStackedLayout | Stacked (one visible at a time) | Wizards, tabbed interfaces              |
| QSplitter      | Resizable panels                | Split views (file explorers, editors)   |

---

## Nesting Layouts

You can nest layouts inside each other to create complex, responsive interfaces. For example, a horizontal layout might
contain several vertical layouts, each managing a column of widgets[1][2].

---

## Choosing a Layout

- Use **QVBoxLayout** or **QHBoxLayout** for simple linear arrangements.
- Use **QGridLayout** for tabular or matrix-like layouts.
- Use **QFormLayout** for clean, two-column forms.
- Use **QStackedLayout** when you need to swap between multiple views in the same space.
- Use **QSplitter** for resizable panels.

These layout managers ensure your application looks professional and adapts gracefully to window resizing[6][7].

??? note "References"
      - [1] https://www.pythonguis.com/tutorials/pyqt6-layouts/
      - [2] https://www.youtube.com/watch?v=Cc_zaUbF4LM
      - [3] https://realpython.com/python-pyqt-layout/
      - [4] https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/
      - [5] https://zetcode.com/pyqt6/layout/
      - [6] https://doc.qt.io/qt-6/layout.html
      - [7] https://doc.qt.io/qt-6/qtwidgets-layouts-basiclayouts-example.html
      - [8] https://doc.qt.io/qtforpython-6/overviews/qtquicklayouts-overview.html
      - [9] https://doc.qt.io/qt-6/qlayout.html
      - [10] https://www.youtube.com/live/trpI4ezSnlQ
      - [11] https://www.reddit.com/r/learnpython/comments/1f4xidk/really_confused_with_pyqt6_layout_management/
      - [12] https://www.youtube.com/watch?v=_16NK5LZPes
      - [13] https://stackoverflow.com/questions/75924821/how-to-keep-layouts-in-a-horizontal-layout-the-same-size-pyqt
      - [14] https://www.youtube.com/watch?v=cLoeJ7UVNno
      - [15] https://www.youtube.com/watch?v=trpI4ezSnlQ
      - [16] https://stackoverflow.com/questions/67307726/pyqt6-confused-about-nesting-layouts-or-widgets
      - [17] https://doc.qt.io/qtforpython-6.5/overviews/layout.html

---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.