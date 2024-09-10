class Agent:
    def __init__(self):
        self.x = random(17, width - 17)
        self.y = random(17, height - 17)
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
        self.radius = random(8, 16)
        self.diam = 2 * self.radius
        
    def update(self):
        self.update_by_velocity()
        self.bounce_boundary()
    
    def bounce_boundary(self):
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= height or self.y - self.radius <= 0:
            self.vy *= -1
            
    def update_by_velocity(self):
        self.x += self.vx
        self.y += self.vy
        
    def draw_agent(self):
        ellipse(self.x, self.y, self.diam, self.diam)
        
    def draw(self):
        if current_mode == POINT_MODE:
            stroke(0)
            self.draw_point()
        elif current_mode == OVERLAP_MODE:
            stroke(0, 16)
            noFill()
            self.draw_overlap()
        
    def draw_point(self):
        point(self.x, self.y)
        
    def draw_overlap(self):
        for other_agent in agents:
            if self != other_agent:
                t_dist = dist(self.x, self.y, other_agent.x, other_agent.y)
                if t_dist < self.radius + other_agent.radius:
                    cx = (self.x + other_agent.x) / 2
                    cy = (self.y + other_agent.y) / 2
                    ellipse(cx, cy, t_dist, t_dist)
                    
max_agents = 32
agents = []
    
AGENT_MODE = 0
POINT_MODE = 1
OVERLAP_MODE = 2

current_mode = AGENT_MODE
  
def setup():
    size(800, 600)
    global agents
    for _ in range(max_agents):
        agents.append(Agent())
            
def draw():
    global current_mode
    for agent in agents:
        agent.update()

    if current_mode == AGENT_MODE:
        background(220, 20, 120)
        noStroke()
        fill(255)
        for agent in agents:
            agent.draw_agent()
    else:
        for agent in agents:
            agent.draw()
                
def mouseClicked():
    global current_mode
    current_mode = (current_mode + 1) % 3
    if current_mode != AGENT_MODE:
        background(255)
