package vista;
import javax.swing.*;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import javax.swing.table.TableColumnModel;

import java.awt.geom.*;
import javax.swing.border.*;
import java.awt.*;


import java.awt.*;

public class VentanaP extends JFrame {
    public VentanaP() {

        super("Inbox - Umail");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setSize(1280, 720);
        this.setLocationRelativeTo(null);
        
        this.setExtendedState(JFrame.MAXIMIZED_BOTH);
        this.getContentPane().setLayout(new GridBagLayout());
        
        this.getContentPane().setBackground(new Color(250, 248, 248));
        
        GridBagConstraints reglas= new GridBagConstraints();

        
        //////top
        JPanel top= new JPanel(new GridBagLayout());
        top.setBackground(new Color(14, 96, 122));
        top.setPreferredSize(new Dimension(0, 30));
        reglas.gridx = 3;
        reglas.gridy = 0;
        reglas.weightx = 1.0;
        reglas.weighty = 1.0;
        reglas.fill = GridBagConstraints.HORIZONTAL;
        reglas.anchor = GridBagConstraints.NORTH;
        
        JLabel titulo = new JLabel("Recibiste XX correos nuevos desde tu última sesión");
        titulo.setForeground(Color.WHITE);
        titulo.setFont(titulo.getFont().deriveFont(Font.PLAIN, 20f));
        titulo.setHorizontalAlignment(SwingConstants.LEFT);
        top.add(titulo);
 
        this.add(top, reglas);
        
        
        JPanel logoPanel = new JPanel(new GridBagLayout());
        logoPanel.setOpaque(false);
        reglas.gridx= 0;
        reglas.gridy= 0;
        reglas.weightx= 0.0;
        reglas.weighty= 0.0;
        
        JLabel logo = new JLabel(); // 
        logo.setPreferredSize(new Dimension(50, 50));
        logo.setBorder(new LineBorder(new Color(14, 96, 122), 0));
        logo.setIcon(createSquareIcon(new Color(14, 96, 122), 50, 50));
        logoPanel.add(Box.createHorizontalStrut(20));
        logoPanel.add(logo);
        logoPanel.add(Box.createHorizontalStrut(20));
        this.add(logoPanel, reglas);
        
        
        //////izquierda
        JPanel pIzquierda = new JPanel();
        reglas.gridx= 0;
        reglas.gridy= 3;
        reglas.weightx= 0.0;
        reglas.weighty= 0.0;
        pIzquierda.setBackground(new Color(250, 248, 248));
        pIzquierda.setLayout(new GridBagLayout());
        
        
        JPanel mid = new JPanel();
        mid.setOpaque(false);
        mid.setLayout(new BoxLayout(mid, BoxLayout.Y_AXIS));

        JButton bRedactar = new JButton(" ✎  Redactar");
        bRedactar.setAlignmentX(Component.LEFT_ALIGNMENT);
        bRedactar.setMaximumSize(new Dimension(200, 56));
        bRedactar.setBackground(new Color(158, 205, 225));
        bRedactar.setForeground(Color.BLACK);
        bRedactar.setFont(bRedactar.getFont().deriveFont(Font.BOLD, 18f));
        bRedactar.setBorder(new CompoundBorder(new LineBorder(new Color(14, 96, 122), 0, true),
                new EmptyBorder(10, 12, 10, 12)));
        mid.add(bRedactar);
        mid.add(Box.createRigidArea(new Dimension(0, 30)));
        
        JPanel folders = new JPanel();
        folders.setLayout(new BoxLayout(folders, BoxLayout.Y_AXIS));
        folders.setBackground(new Color(22, 96, 136));
        
       

        String[] folderNames = { "Inbox", "Enviados", "Borradores", "Archivados", "Papelera", "Personal" };
        for (int i = 0; i < folderNames.length; i++) {
            JButton btn = new JButton(folderNames[i]);
            btn.setAlignmentX(Component.LEFT_ALIGNMENT);
            btn.setMaximumSize(new Dimension(200, 42));
            btn.setMinimumSize(new Dimension(120, 42));
            btn.setBackground(i == 0 ? new Color(14, 96, 122) : new Color(14, 96, 122)); // same color, will adjust text
            btn.setForeground(Color.WHITE);
            btn.setFocusPainted(false);
            btn.setBorder(new EmptyBorder(8, 12, 8, 12));
            btn.setFont(btn.getFont().deriveFont(Font.PLAIN, 16f));
            if (i == 0) {
                // highlight first folder differently (simulate selected)
                btn.setBackground(new Color(19, 101, 128));
                btn.setOpaque(true);
            }
            folders.add(btn);
            folders.add(Box.createRigidArea(new Dimension(0, 8)));
        }
        
        mid.add(folders);
        pIzquierda.add(mid);
        this.add(pIzquierda, reglas);
        
        /////centro
        JPanel pCentro = new JPanel();
        reglas.gridx= 3;
        reglas.gridy= 3;
        reglas.weightx= 0.0;
        reglas.weighty= 0.0;
        pCentro.setBackground(new Color(250, 248, 248));
        pCentro.setBorder(new EmptyBorder(12, 12, 12, 12));
        pCentro.setLayout(new BorderLayout());
     
     // Toolbar with filter icons (visual)
        JPanel toolbar = new JPanel(new BorderLayout());
        toolbar.setOpaque(false);
        JPanel leftTools = new JPanel(new FlowLayout(FlowLayout.LEFT, 8, 6));
        leftTools.setOpaque(false);

        String[] toolIcons = { "⎘", "☰", "⤓", "⚙" };
        for (String t : toolIcons) {
            JLabel lbl = new JLabel(t);
            lbl.setOpaque(true);
            lbl.setBackground(new Color(217, 236, 239));
            lbl.setBorder(new EmptyBorder(8, 12, 8, 12));
            lbl.setFont(lbl.getFont().deriveFont(16f));
            leftTools.add(lbl);
        }

        toolbar.add(leftTools, BorderLayout.WEST);
        pCentro.add(toolbar, BorderLayout.NORTH);

        // Message list (table-like)
        JTable table = createMessageTable();
        JScrollPane scroll = new JScrollPane(table);
        scroll.setBorder(new CompoundBorder(new EmptyBorder(8, 0, 0, 0),
                new LineBorder(new Color(180, 200, 203), 2, true)));
        pCentro.add(scroll, BorderLayout.CENTER);
        
        this.add(pCentro, reglas);
    }
    
    private JTable createMessageTable() {
        // Columns: Select, Subject, Preview, Date
        String[] columns = { "", "Asunto", "Previsualización", "Fecha" };

        Object[][] data = new Object[14][4];
        for (int i = 0; i < data.length; i++) {
            data[i][0] = Boolean.FALSE;
            data[i][1] = "<html><b>Lorem Ipsum Lorem Ip...</b></html>";
            data[i][2] = "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum...";
            data[i][3] = "09/11/2025";
        }

        DefaultTableModel model = new DefaultTableModel(data, columns) {
            @Override
            public Class<?> getColumnClass(int columnIndex) {
                if (columnIndex == 0) return Boolean.class;
                return String.class;
            }

            @Override
            public boolean isCellEditable(int row, int col) {
                // not editable for this mockup
                return false;
            }
        };

        JTable table = new JTable(model);
        table.setRowHeight(64);
        table.setFillsViewportHeight(true);
        table.setShowGrid(true);
        table.setGridColor(new Color(180, 200, 203));
        table.setIntercellSpacing(new Dimension(2, 2));
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        // Column sizing
        TableColumnModel cm = table.getColumnModel();
        cm.getColumn(0).setPreferredWidth(40);  // checkbox
        cm.getColumn(1).setPreferredWidth(320); // subject
        cm.getColumn(2).setPreferredWidth(760); // preview
        cm.getColumn(3).setPreferredWidth(120); // date

        // Renderers for styling
        // 1) Subject column - HTML already bold; customize background
        DefaultTableCellRenderer subjectRenderer = new DefaultTableCellRenderer() {
            private final Color rowBg = new Color(226, 240, 243); // pale blue row
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                                                           boolean isSelected, boolean hasFocus,
                                                           int row, int column) {
                JLabel lbl = (JLabel) super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                lbl.setBackground(rowBg);
                lbl.setOpaque(true);
                lbl.setBorder(new EmptyBorder(6, 10, 6, 10));
                lbl.setFont(lbl.getFont().deriveFont(18f));
                return lbl;
            }
        };

        // 2) Preview column
        DefaultTableCellRenderer previewRenderer = new DefaultTableCellRenderer() {
            private final Color rowBg = new Color(226, 240, 243);
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                                                           boolean isSelected, boolean hasFocus,
                                                           int row, int column) {
                JLabel lbl = (JLabel) super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                lbl.setBackground(rowBg);
                lbl.setOpaque(true);
                lbl.setForeground(new Color(102, 115, 118));
                lbl.setBorder(new EmptyBorder(6, 6, 6, 6));
                lbl.setFont(lbl.getFont().deriveFont(14f));
                return lbl;
            }
        };

        // 3) Date column - right aligned
        DefaultTableCellRenderer dateRenderer = new DefaultTableCellRenderer() {
            private final Color rowBg = new Color(226, 240, 243);
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                                                           boolean isSelected, boolean hasFocus,
                                                           int row, int column) {
                JLabel lbl = (JLabel) super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                lbl.setBackground(rowBg);
                lbl.setOpaque(true);
                lbl.setHorizontalAlignment(SwingConstants.RIGHT);
                lbl.setBorder(new EmptyBorder(6, 6, 6, 10));
                lbl.setFont(lbl.getFont().deriveFont(13f));
                lbl.setForeground(new Color(83, 96, 98));
                return lbl;
            }
        };

        // Checkbox column renderer background
        DefaultTableCellRenderer checkboxBg = new DefaultTableCellRenderer() {
            private final Color rowBg = new Color(226, 240, 243);
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                                                           boolean isSelected, boolean hasFocus,
                                                           int row, int column) {
                JCheckBox chk = new JCheckBox();
                chk.setSelected(Boolean.TRUE.equals(value));
                chk.setHorizontalAlignment(SwingConstants.CENTER);
                chk.setBackground(rowBg);
                chk.setBorder(new EmptyBorder(6, 6, 6, 6));
                chk.setEnabled(false);
                return chk;
            }
        };

        cm.getColumn(0).setCellRenderer(checkboxBg);
        cm.getColumn(1).setCellRenderer(subjectRenderer);
        cm.getColumn(2).setCellRenderer(previewRenderer);
        cm.getColumn(3).setCellRenderer(dateRenderer);

        // Remove table header look to mimic the design (but keep it visible minimal)
        JTableHeader header = table.getTableHeader();
        header.setReorderingAllowed(false);
        header.setPreferredSize(new Dimension(header.getPreferredSize().width, 0)); // hide header height
        header.setVisible(false);

        // Alternating row - handled by renderer background consistently
        table.setBackground(new Color(226, 240, 243));

        return table;
    }

	private Icon createSquareIcon(Color color, int w, int h) {
		BufferedImageIcon bi = new BufferedImageIcon(w, h, color);
        return bi;
	}
	 private static class BufferedImageIcon implements Icon {
	        private final int w, h;
	        private final Color color;
	        public BufferedImageIcon(int w, int h, Color color) {
	            this.w = w; this.h = h; this.color = color;
}
			@Override
			public void paintIcon(Component c, Graphics g, int x, int y) {
				 Graphics2D g2 = (Graphics2D) g.create();
		            g2.setColor(color);
		            g2.fillRoundRect(x, y, w, h, 10, 10);
		            g2.setColor(Color.WHITE);
		            g2.setStroke(new BasicStroke(3f));
		            // simple glyph placeholder
		            g2.drawLine(x + 14, y + 20, x + w - 14, y + 20);
		            g2.drawLine(x + 14, y + 40, x + w - 14, y + 40);
		            g2.dispose();
			}
			@Override
			public int getIconWidth() {
				// TODO Auto-generated method stub
				return w;
			}
			@Override
			public int getIconHeight() {
				// TODO Auto-generated method stub
				return h;
			}
	 }
}