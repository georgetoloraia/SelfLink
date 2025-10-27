// Matrix animation
const c=document.getElementById('matrix'),ctx=c.getContext('2d');
function resize(){c.width=innerWidth;c.height=innerHeight;}
window.addEventListener('resize',resize);resize();
let pts=Array.from({length:70},()=>({x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4}));
function draw(){
ctx.clearRect(0,0,c.width,c.height);
for(let p of pts){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>c.width)p.vx*=-1;if(p.y<0||p.y>c.height)p.vy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,2,0,Math.PI*2);ctx.fillStyle='#74b9ff';ctx.fill();}
for(let i=0;i<pts.length;i++){for(let j=i+1;j<pts.length;j++){let dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y,d=Math.hypot(dx,dy);if(d<140){ctx.strokeStyle=`rgba(124,185,255,${1-d/140})`;ctx.lineWidth=.5;ctx.beginPath();ctx.moveTo(pts[i].x,pts[i].y);ctx.lineTo(pts[j].x,pts[j].y);ctx.stroke();}}}
requestAnimationFrame(draw);}
draw();

// Simple routing by anchors
document.querySelectorAll('.links a').forEach(a=>{
 a.addEventListener('click',e=>{
  e.preventDefault();
  const id=a.getAttribute('href').substring(1);
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
 });
});