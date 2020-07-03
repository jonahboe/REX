import g4p_controls.*;

class ToolBar {
  color ORANGE = color(226,163,28);
  color RED = color(255,0,0);
  
  int xPos;
  int yPos;
  int wide;
  int high;
  
  GTextField lat1;
  GTextField lat2;
  GTextField lon1;
  GTextField lon2;
  
  public ToolBar(PApplet parent, int x, int y, int w, int h) {
    this.xPos = x;
    this.yPos = y;
    this.wide = w;
    this.high = h;
    
    lat1 = new GTextField(parent, x + 40, y + 10, wide - 50, 20);
    lat1.tag = "lat1";
    lat1.setPromptText("Enter latitude 1");
    
    lon1 = new GTextField(parent, x + 40, y + 40, wide - 50, 20);
    lon1.tag = "lon1";
    lon1.setPromptText("Enter longitude 1");
    
    lat2 = new GTextField(parent, x + 40, y + 80, wide - 50, 20);
    lat2.tag = "lat2";
    lat2.setPromptText("Enter latitude 2");
    
    lon2 = new GTextField(parent, x + 40, y + 110, wide - 50, 20);
    lon2.tag = "lon2";
    lon2.setPromptText("Enter longitude 2");
  }
  
  void update() {
    // Tool box
    noStroke();
    fill(88, 175, 215);
    rect(xPos, yPos, wide, high,10);
    
    // Section divs
    stroke(0);
    strokeWeight(1);
    line(xPos + 5, yPos + 70, xPos + wide - 5, yPos + 70);
    line(xPos + 5, yPos + 140, xPos + wide - 5, yPos + 140);
    
    // Location Selectors
    noStroke();
    fill(255);
    rect(xPos+10,yPos+25,20,20,5);
    rect(xPos+10,yPos+95,20,20,5);
    drawTarget(xPos + 20, yPos + 35, RED);
    drawTarget(xPos + 20, yPos + 105, ORANGE);
  }
  
  void drawTarget(int x, int y, color c) {
    noFill();
    stroke(c);
    strokeWeight(1);
    ellipse(x, y, 12, 12);
    line(x-6, y, x+6, y);
    line(x, y-6, x, y+6);
  }
  
}
