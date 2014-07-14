import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

//Constructor for UI window

public class sdk_ui extends JFrame implements ActionListener {
  int num_functions = 6;
  private JPanel ui_panel = new JPanel();
  private JButton[] function_buttons = new JButton[num_functions];
  private JButton[] statement_buttons = new JButton[5];
  private JButton[] num_pad = new JButton[10];
  private JButton[] operator_buttons = new JButton[3];
  private JButton enter_button = new JButton("Enter");
  private JButton end_statement = new JButton("End");
  private JTextField strings = new JTextField("Enter String Here");
  private String[] function_names = new String[num_functions];
  private JButton done_button = new JButton("done");
  private JTextArea codeTxt = new JTextArea(35, 50);
  private JScrollPane codeScrollPane = new JScrollPane(codeTxt);
  //private JLabel functions = new JLabel("Functions");
  //private JLabel statements = new JLabel("Statements");
  private Vector<JTextArea> textFieldVector = new Vector<JTextArea>();
  private File temp_name = new File("temp_file.txt");
  private File file_name = new File("Your_textfile.py");
  private Scanner sc_line;
  int num_ints = 0, num_strings = 0;
  boolean functions = false, loop = false;

  sdk_ui() {
    super("SDK Interface"); 
    setBounds(500,500,1500,1500);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container con = this.getContentPane(); // inherit main frame
    con.add(ui_panel); // add the panel to frame

    textFieldVector.add(codeTxt);
    con.add(codeTxt, BorderLayout.PAGE_END);
    con.revalidate();
    con.repaint();
    //ui_panel.add(codeTxt);
    
    for(int i = 0; i < function_buttons.length; i++) {
      switch (i) {
        case 0: function_buttons[i] = new JButton("Scan cars");
                break;
        case 1: function_buttons[i] = new JButton("Connect car");
                break;
        case 2: function_buttons[i] = new JButton("Set lights");
                break;
        case 3: function_buttons[i] = new JButton("Set speed");
                break;
        case 4: function_buttons[i] = new JButton("Change lane");
                break;
        case 5: function_buttons[i] = new JButton("Disconnect car");
                break;
      }
      function_names[i] = function_buttons[i].getText();
      function_names[i] = function_names[i].replace(" ", "_");
      function_buttons[i].addActionListener(this);
      ui_panel.add(function_buttons[i]);

    }
    for(int i = 0; i < statement_buttons.length; i++) {
      switch (i) {
        case 0: statement_buttons[i] = new JButton("for");
                break;
        case 1: statement_buttons[i] = new JButton("while");
                break;
        case 2: statement_buttons[i] = new JButton("if");
                break;
        case 3: statement_buttons[i] = new JButton("else");
                statement_buttons[i].setEnabled(false);
                break;
        case 4: statement_buttons[i] = new JButton("else if");
                statement_buttons[i].setEnabled(false);
                break;
      }
      statement_buttons[i].addActionListener(this);
      ui_panel.add(statement_buttons[i]);
    }
    end_statement = new JButton("end");
    end_statement.addActionListener(this);
    end_statement.setEnabled(false);
    ui_panel.add(end_statement);
    
    for(int i = 0; i < num_pad.length; i++) {
      switch(i) {
        case 0: num_pad[i] = new JButton(i+"");
                break;
        case 1: num_pad[i] = new JButton(i+"");
                break;
        case 2: num_pad[i] = new JButton(i+"");
                break;
        case 3: num_pad[i] = new JButton(i+"");
                break;
        case 4: num_pad[i] = new JButton(i+"");
                break;
        case 5: num_pad[i] = new JButton(i+"");
                break;
        case 6: num_pad[i] = new JButton(i+"");
                break;
        case 7: num_pad[i] = new JButton(i+"");
                break;
        case 8: num_pad[i] = new JButton(i+"");
                break;
        case 9: num_pad[i] = new JButton(i+"");
                break;
      }
      num_pad[i].addActionListener(this);
      num_pad[i].setEnabled(false);
      ui_panel.add(num_pad[i]);
    }
    for(int i = 0; i < operator_buttons.length; i++){
      switch(i) {
        case 0: operator_buttons[i] = new JButton("<");
                break;
        case 1: operator_buttons[i] = new JButton(">");
                break;
        case 2: operator_buttons[i] = new JButton("=");
                break;
      }
      operator_buttons[i].addActionListener(this);
      operator_buttons[i].setEnabled(false);
      ui_panel.add(operator_buttons[i]);
    }
    enter_button.addActionListener(this);
    enter_button.setEnabled(false);
    ui_panel.add(enter_button);
   	done_button.addActionListener(this);
   	ui_panel.add(done_button);
   	ui_panel.add(strings);
   	strings.setEditable(false);
    codeTxt.setFont(new Font("Times New Roman", Font.BOLD, 12));
    codeTxt.setLineWrap(true);
    codeTxt.setWrapStyleWord(true);
    codeScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
    codeScrollPane.setPreferredSize(new Dimension(250, 250));
    
    setVisible(true); // display this frame
  }

  public void actionPerformed(ActionEvent e) {
    int caretPos = codeTxt.getCaretPosition();
    
    if(e.getSource() == function_buttons[0]) {
      textInsert(function_buttons[0].getText(), false);
      num_ints = 1;
      num_strings = 1;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == function_buttons[1]) {
      textInsert(function_buttons[1].getText(), false);
      num_strings = 2;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == function_buttons[2]) {
      textInsert(function_buttons[2].getText(), false);
      num_strings = 3;
      num_ints = 3;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == function_buttons[3]) {
      textInsert(function_buttons[3].getText(), false);
      num_ints = 2;
      num_strings = 1;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == function_buttons[4]) {
      textInsert(function_buttons[4].getText(), false);
      num_ints = 2;
      num_strings = 1;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    } 
    else if(e.getSource() == function_buttons[function_buttons.length - 1]) {
      textInsert(function_buttons[5].getText(), false);
      num_strings = 1;
      strings.setEditable(true);
      functions = true;
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == statement_buttons[0]) {
      textInsert(statement_buttons[0].getText(), true);
      codeTxt.insert(" x in range(", codeTxt.getCaretPosition());
      all_buttons_switch(function_buttons, false);
      all_buttons_switch(statement_buttons, false);
      all_buttons_switch(num_pad, true);
      num_ints = 2;
      loop = true;
    }
    else if(e.getSource() == statement_buttons[1]) {
      textInsert(statement_buttons[1].getText(), true);
      loop = true;
    }
    else if(e.getSource() == statement_buttons[2]) {
      textInsert(statement_buttons[2].getText(), true);
    }
    else if(e.getSource() == statement_buttons[3]) {
      textInsert(statement_buttons[3].getText(), true);
    }
    else if(e.getSource() == statement_buttons[statement_buttons.length - 1]) {
      textInsert(statement_buttons[statement_buttons.length-1].getText(), true);
    }
    else if(e.getSource() == end_statement) {
      codeTxt.insert("//End\n", caretPos);
      end_statement.setEnabled(false);
      all_buttons_switch(num_pad, false);
    }
    else if(e.getSource() == num_pad[0]) {
      codeTxt.insert(num_pad[0].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[1]) {
      codeTxt.insert(num_pad[1].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[2]) {
      codeTxt.insert(num_pad[2].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[3]) {
      codeTxt.insert(num_pad[3].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[4]) {
      codeTxt.insert(num_pad[4].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[5]) {
      codeTxt.insert(num_pad[5].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[6]) {
      codeTxt.insert(num_pad[6].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[7]) {
      codeTxt.insert(num_pad[7].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[8]) {
      codeTxt.insert(num_pad[8].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == num_pad[9]) {
      codeTxt.insert(num_pad[9].getText(), caretPos);
      enter_button.setEnabled(true);
    }
    else if(e.getSource() == operator_buttons[0]) {
      codeTxt.insert(num_pad[0].getText(), caretPos);
    }
    else if(e.getSource() == operator_buttons[1]) {
      codeTxt.insert(num_pad[1].getText(), caretPos);
    }
    else if(e.getSource() == operator_buttons[2]) {
      for(int i = 0; i < 2; i++) {
        codeTxt.insert(num_pad[2].getText(), caretPos);
      }
    }
    else if(e.getSource() == enter_button) {
      if(num_strings > 0) {
        num_strings--;
        codeTxt.insert(strings.getText(), codeTxt.getCaretPosition());
        if(num_strings == 0 && num_ints == 0){
          codeTxt.insert(")\n", codeTxt.getCaretPosition());
          functions = false;
          all_buttons_switch(function_buttons, true);
          all_buttons_switch(num_pad, false);
          enter_button.setEnabled(false);
          done_button.setEnabled(true);
        }
        else {
          codeTxt.insert(", ", codeTxt.getCaretPosition());
          if(num_strings == 0) {
            strings.setEditable(false);
            all_buttons_switch(num_pad, true);
            num_ints--;
          }
        }
      }
      else if(num_ints == 0) {
        if(functions){
          codeTxt.insert(")\n", caretPos);
          functions = false;
          all_buttons_switch(function_buttons, true);
          all_buttons_switch(num_pad, false);
          enter_button.setEnabled(false);
          done_button.setEnabled(true);
        }
        else if(loop) {
          codeTxt.insert("):\n", caretPos);
          loop = false;
          all_buttons_switch(function_buttons, true);
          all_buttons_switch(num_pad, false);
          end_statement.setEnabled(true);
        }
        else {
          codeTxt.insert(":\n", caretPos);
          end_statement.setEnabled(true);
        }
      } else {
        codeTxt.insert(", ", caretPos);
      }
      enter_button.setEnabled(false);
    }
    else {
      write_file();
      parse_tabs();
      all_buttons_switch(function_buttons, true);
    }

  }

  public void textInsert(String txt, boolean type) {
    int caretPos = codeTxt.getCaretPosition();
    if(!type) {
    	codeTxt.insert(txt.replace(" ", "_") + "(", caretPos);
    	all_buttons_switch(function_buttons, false);
    	done_button_switch(false);
    	all_buttons_switch(statement_buttons, false);
    }
    else {
      codeTxt.insert(txt + " ", caretPos);
      all_buttons_switch(statement_buttons, false);
      all_buttons_switch(function_buttons, false);
      all_buttons_switch(num_pad, true);
      done_button_switch(false);
    }
  }
  public void all_buttons_switch(JButton[] buttons, boolean active) {
    if(!active) {
      for(int i = 0; i < buttons.length; i++){
        buttons[i].setEnabled(false);
      }
    } 
    else {
      for(int i = 0; i < buttons.length; i++){
        buttons[i].setEnabled(true);
      }
    }
  }
  
  public void done_button_switch(boolean active) {
    if(active) {
      done_button.setEnabled(true);
    }
    else {
      done_button.setEnabled(false);
    }
  }
  public void write_file() {
    try {
      FileWriter temp = new FileWriter(temp_name);
      FileWriter prog = new FileWriter(file_name);
      sc_line = new Scanner(temp_name);
      String pars;
      int tabCount = 1;
      prog.write("#!/usr/bin/python\nimport SDK.py\ndef main()\n\tANKI_start()\n");
      codeTxt.write(temp);
      while (sc_line.hasNextLine()) {
        pars = sc_line.nextLine();
        pars = pars.replace("\t", "");
        for(int i = 0; i < num_functions; i++) {
          //System.out.println(function_names[i]);
          pars = pars.replace(function_names[i], "ANKI." + function_names[i]);
        }
        prog.write("\t"+pars+"\n");
      }
      prog.write("\tANKI_end()\n");
      prog.write("main()");
      prog.close();
      temp_name.delete();
    } catch(IOException e) {
      e.printStackTrace();
    }
  }

  public void parse_tabs() {
    
  } 

  public static void main(String args[]) {
    new sdk_ui();
  }
}
