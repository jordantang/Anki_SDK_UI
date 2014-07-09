//package layout;

import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

//Constructor for UI window

public class sdk_ui extends JFrame implements ActionListener {
  int num_buttons = 7;
  private JPanel ui_panel = new JPanel();
  private JFrame ui_frame = new JFrame();
  private JButton[] function_buttons = new JButton[num_buttons];
  private JTextArea codeTxt = new JTextArea(25, 50);
  private JLabel functions, statements;
  private JScrollPane codeScrollPane = new JScrollPane(codeTxt);
  private Vector textFieldVector = new Vector();
  private File temp_name = new File("temp_file.txt");
  private File file_name = new File("Your_textfile.py");

  sdk_ui() {
    super("SDK Interface"); 
    setBounds(0,0,1000,1000);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container con = this.getContentPane(); // inherit main frame
    con.add(ui_frame); // add the panel to frame

    textFieldVector.add(codeTxt);
    con.add(codeTxt, BorderLayout.PAGE_END);
    con.revalidate();
    con.repaint();
    CardLayoutTest cd = new CardLayoutTest();
    cd.addComponentToPane(ui_frame.getContentPane());
    ui_frame.pack();
    ui_frame.setVisible(true);
    //ui_panel.add(codeTxt);
    /*functions = new JLabel("Functions");
    functions.setLocation(0, 50);
    statements = new JLabel("Statements");
    statements.setLocation(0, 50);
    for(int i = 0; i < num_buttons; i++) {
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
        case 6: function_buttons[i] = new JButton("Done");
                break;
      } 
      function_buttons[i].setLocation(50*i,50);
      function_buttons[i].setSize(100, 30);
      function_buttons[i].addActionListener(this);
      ui_panel.add(function_buttons[i]);
      ui_panel.add(functions);
      ui_panel.add(statements);
    }

    codeTxt.setFont(new Font("Times New Roman", Font.BOLD, 12));
    codeTxt.setLineWrap(true);
    codeTxt.setWrapStyleWord(true);
    codeScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
    codeScrollPane.setPreferredSize(new Dimension(250, 250));
    
    setVisible(true);*/
  } 

  class CardLayoutTest implements ItemListener {
    JPanel cards;
    final static String BUTTONPANEL = "Card with JButtons";
    final static String LABELPANEL = "Card with JLabels";
    int num_buttons = 7;
    JButton function_buttons[] = new JButton[num_buttons];

    public void addComponentToPane(Container pane) {
      JPanel comboBoxPane = new JPanel();
      String comboBoxItems[] = { BUTTONPANEL, LABELPANEL };
      JComboBox cb = new JComboBox(comboBoxItems);
      cb.setEditable(false);
      cb.addItemListener(this);
      comboBoxPane.add(cb);
      
      JPanel card1 = new JPanel();
      for(int i = 0; i < num_buttons; i++) {
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
          case 6: function_buttons[i] = new JButton("Done");
                  break;
        }
        card1.add(function_buttons[i]);
      }

      JPanel card2 = new JPanel();
      card2.add(new JLabel("Functions"));
      
      cards = new JPanel(new CardLayout());
      cards.add(card1, BUTTONPANEL);
      cards.add(card2, LABELPANEL);

      pane.add(comboBoxPane, BorderLayout.PAGE_START);
      pane.add(cards, BorderLayout.CENTER);
    }

    public void itemStateChanged(ItemEvent evt) {
      CardLayout c1 = (CardLayout)(cards.getLayout());
      c1.show(cards, (String)evt.getItem());
    }
  }

  public void actionPerformed(ActionEvent e) {
    if(e.getSource() == function_buttons[0]) {
      textInsert(function_buttons[0].getText());
      function_buttons[1].setEnabled(false);
    }
    else if(e.getSource() == function_buttons[1]) {
      textInsert(function_buttons[1].getText());
      function_buttons[2].setEnabled(false);
      function_buttons[3].setEnabled(false);
      function_buttons[4].setEnabled(true);
    }
    else if(e.getSource() == function_buttons[2]) {
      textInsert(function_buttons[2].getText());
      function_buttons[4].setEnabled(false);
      function_buttons[1].setEnabled(true);
    }
    else if(e.getSource() == function_buttons[3]) {
      textInsert(function_buttons[3].getText());
      function_buttons[2].setEnabled(true);
      function_buttons[3].setEnabled(true);
      function_buttons[0].setEnabled(false);
    }
    else if(e.getSource() == function_buttons[4]) {
      textInsert(function_buttons[4].getText());
    } 
    else if(e.getSource() == function_buttons[5]) {
      textInsert(function_buttons[5].getText());
      for(int i = 0; i < num_buttons; i++) {
        function_buttons[i].setEnabled(true);
      }
    }
    else {
      write_file();
      parse_tabs();
      for(int i = 0; i < num_buttons; i++) {
        if(!function_buttons[i].isEnabled()) {
          function_buttons[i].setEnabled(true);
        }
      }
    }
  }

  public void textInsert(String txt) {
    int caretPos = codeTxt.getCaretPosition();
    codeTxt.insert(txt.replace(" ", "_") + "()" + "\n", caretPos);
  }

  public void write_file() {
    try {
      FileWriter temp = new FileWriter(temp_name);
      FileWriter prog = new FileWriter(file_name);
      Scanner sc_line = new Scanner(temp_name);
      String pars;
      int tabCount;
      prog.write("#!/usr/bin/python\nimport SDK.py\ndef main()\n\tANKI_start()\n");
      codeTxt.write(temp);
      while (sc_line.hasNextLine()) {
        pars = sc_line.nextLine();
        pars = pars.replace("\t", "");
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
