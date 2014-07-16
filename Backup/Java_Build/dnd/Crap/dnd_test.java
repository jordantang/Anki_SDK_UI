import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

public class dnd_test extends JFrame {
  private JButton test_button;
  private JPanel ui_panel = new JPanel();
  private TransferHandler transfer = new TransferHandler("dnd_test");
  private JTextArea textarea;

  public dnd_test() {
    super("dnd_test");
    setBounds(500, 500, 800, 500);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container con = this.getContentPane();
    con.add(ui_panel);

    setLayout(new FlowLayout());
    test_button = new JButton("Test Drag");
    test_button.setLocation(50,0);
    test_button.setSize(100,30);
    test_button.setTransferHandler(transfer);
    test_button.addMouseListener(new MouseAdapter(){
      public void mousePressed(MouseEvent e){
        JButton test_button = (JButton)e.getSource();
        TransferHandler handle = test_button.getTransferHandler();
        handle.exportAsDrag(test_button, e, TransferHandler.COPY);
        }

     });
    test_button.addMouseListener(new MouseAdapter() {
      @Override
      public void mouseExited(MouseEvent e) {
        System.out.println("mouse released\n");
      }
    });
    textarea = new JTextArea(5, 30);
    ui_panel.add(textarea);
    ui_panel.add(test_button);
    setVisible(true);
  }
  public static void main(String args[]) {
    new dnd_test();
    
  }
}
