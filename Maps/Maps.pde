import drop.*;

SDrop drop;

PImage map;
PVector startPos;
boolean charting;

boolean firstRun;

ToolBar toolBar;

void setup() {
  size(500, 500);
  frameRate(30);
  drop = new SDrop(this);
  noFill();
  
  charting = false;
  startPos = new PVector(-2, -2);
  
  firstRun = true;
  
  // Set up an intro page
  background(255);
}

void draw() {
  if(map != null && map.width > 0) {
    // The main page with image
    surface.setSize(map.width, map.height);
    image(map, 0, 0);
    
    // If selecting area of map
    if (charting) {
      strokeWeight(2);
      stroke(255,0,0);
      noFill();
      rect(startPos.x, startPos.y, mouseX - startPos.x, mouseY - startPos.y);
    }
    
    // Add the toolbar in the right spot
    if (firstRun) {
      toolBar = new ToolBar(this, width - 210, 10, 200, 400);
      firstRun = false;
    }
    
    // Draw the toolbox
    toolBar.update();
  }
}

void mousePressed() {
  if (charting == false)
  {
    startPos = new PVector(mouseX, mouseY);
    charting = true;
  }
}

void mouseReleased() {
  charting = false;
}

void dropEvent(DropEvent theDropEvent) {
  // load the image into our PImage.
  if(theDropEvent.isImage()) {
    println("Loading image ...");
    String path = theDropEvent.toString();
    map = requestImage(path);
  }
}
