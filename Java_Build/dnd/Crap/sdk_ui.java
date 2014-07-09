import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

//Constructor for UI window

public class sdk_ui extends JFrame implements ActionListener {
  JPanel ui_panel = new JPanel();
  JButton[] sdk_buttons = new JButton[6];
  JTextArea codeTxt = new JTextArea(20,50);
  JScrollPane codeScrollPane = new JScrollPane(codeTxt);
  Vector textFieldVector = new Vector();
  TransferHandler transfer;
  int num_buttons = 6;

  sdk_ui() {
    super("SDK Interface"); 
    setBounds(500,500,800,500);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container con = this.getContentPane(); // inherit main frame
    con.add(ui_panel); // add the panel to frame

    textFieldVector.add(codeTxt);
    con.add(codeTxt, BorderLayout.PAGE_END);
    con.revalidate();
    con.repaint();
    
    for(int i = 0; i < num_buttons; i++) {
      if(i < num_buttons - 1) {
        sdk_buttons[i] = new JButton("Test" + i);
      } else {
        sdk_buttons[i] = new JButton("Done");
      }
      transfer = new TransferHandler(sdk_buttons[i].getText());
      sdk_buttons[i].setLocation(50*i,0);
      sdk_buttons[i].setSize(100, 30);
      sdk_buttons[i].setTransferHandler(transfer);
      
      sdk_buttons[i].addMouseListener(new MouseAdapter(){

            public void mousePressed(MouseEvent e){
                JButton button = (JButton)e.getSource();
                TransferHandler handle = button.getTransferHandler();
                handle.exportAsDrag(button, e, TransferHandler.COPY);

            }
        });

      ui_panel.add(sdk_buttons[i]);
    }

    codeTxt.setFont(new Font("Times New Roman", Font.BOLD, 12));
    codeTxt.setLineWrap(true);
    codeTxt.setWrapStyleWord(true);
    codeScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
    codeScrollPane.setPreferredSize(new Dimension(250, 250));
    
    setVisible(true); // display this frame
  }

  public void actionPerformed(ActionEvent e) {
    if(e.getSource() == sdk_buttons[0]) {
      textInsert(sdk_buttons[0].getText());
    }
    else if(e.getSource() == sdk_buttons[1]) {
      textInsert(sdk_buttons[1].getText());
    }
    else if(e.getSource() == sdk_buttons[2]) {
      textInsert(sdk_buttons[2].getText());
    }
    else if(e.getSource() == sdk_buttons[3]) {
      textInsert(sdk_buttons[3].getText());
    }
    else if(e.getSource() == sdk_buttons[4]) {
      textInsert(sdk_buttons[4].getText());
    } 
    else if(e.getSource() == sdk_buttons[5]) {
      write_file();
    }
  }

  public void textInsert(String txt) {
    int caretPos = codeTxt.getCaretPosition();
    codeTxt.insert(txt+ "\n", caretPos);
  }

  public void write_file() {
    try {
      FileWriter prog = new FileWriter("Your_Program.txt");
      codeTxt.write(prog);
    } catch(IOException e) {
      e.printStackTrace();
    }
  }

  public static void main(String args[]) {
    new sdk_ui();
  }
}
