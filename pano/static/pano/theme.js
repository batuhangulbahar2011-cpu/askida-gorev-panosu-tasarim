(() => {
  'use strict';
  const root = document.documentElement;
  const key = 'askida-theme';
  let theme = 'light';
  try { if (localStorage.getItem(key) === 'dark') theme = 'dark'; } catch (_) {}
  root.dataset.theme = theme;
  function apply(next, remember = false) {
    theme = next === 'dark' ? 'dark' : 'light';
    root.dataset.theme = theme;
    if (remember) { try { localStorage.setItem(key, theme); } catch (_) {} }
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.setAttribute('aria-checked', String(theme === 'dark'));
      button.title = theme === 'dark' ? 'Açık moda geç' : 'Koyu moda geç';
      button.querySelector('.theme-label').textContent = theme === 'dark' ? 'Açık mod' : 'Koyu mod';
      button.querySelector('.theme-icon').textContent = theme === 'dark' ? '☀' : '☾';
    }
  }
  window.addEventListener('storage', event => {
    if (event.key === key) apply(event.newValue);
  });
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('theme-toggle');
    button.hidden = false;
    apply(theme);
    button.addEventListener('click', () => apply(theme === 'dark' ? 'light' : 'dark', true));
    const menu = document.getElementById('menu-toggle');
    if (menu) {
      function setMenu(open) {
        root.dataset.navOpen = String(open);
        menu.setAttribute('aria-expanded', String(open));
      }
      setMenu(false);
      root.dataset.navReady = 'true';
      menu.hidden = false;
      menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
      document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true' && window.matchMedia('(max-width:850px)').matches) {
          setMenu(false); menu.focus();
        }
      });
    }
    const canvas = document.getElementById('ambient-shader');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    // Küçük çizim yüzeyi, düşük kare hızı; destek yoksa CSS zemini kalır.
    if (motion.matches || navigator.connection?.saveData) return;
    let gl;
    try { gl = canvas.getContext('webgl', { alpha: false, antialias: false, depth: false, stencil: false, powerPreference: 'low-power' }); } catch (_) { return; }
    if (!gl) return;
    function compile(type, source) {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source); gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) { gl.deleteShader(shader); return null; }
      return shader;
    }
    const vertex = compile(gl.VERTEX_SHADER, 'attribute vec2 p;varying vec2 uv;void main(){uv=p*.5+.5;gl_Position=vec4(p,0.,1.);}');
    const fragment = compile(gl.FRAGMENT_SHADER, `precision mediump float;
      varying vec2 uv;uniform float t;uniform float dark;
      void main(){
        vec2 p=uv;float wave=sin(p.x*5.5+t*.22)*.07;
        float glow=exp(-length((p-vec2(.78,.72+wave))*vec2(1.1,1.8))*4.);
        float ribbon=exp(-abs(p.y-.68-sin(p.x*4.+t*.18)*.12)*17.)*.24;
        vec3 color=mix(vec3(.22,.55,.36),vec3(.45,.48,.53),dark);
        // Opak çizim + CSS opacity: sürücünün alpha birleştirmesine bağlı değil.
        vec3 base=mix(vec3(.961,.969,.957),vec3(.067,.071,.086),dark);
        gl_FragColor=vec4(mix(base,color,clamp(glow+ribbon,0.,1.)),1.);
      }`);
    if (!vertex || !fragment) return;
    const program = gl.createProgram();
    gl.attachShader(program, vertex); gl.attachShader(program, fragment); gl.linkProgram(program);
    gl.deleteShader(vertex); gl.deleteShader(fragment);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) { gl.deleteProgram(program); return; }
    gl.useProgram(program);
    const buffer = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,1,1]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, 'p'); gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    const clock = gl.getUniformLocation(program, 't'), mode = gl.getUniformLocation(program, 'dark');
    let timer = null, lost = false, time = 0;
    function resize() {
      canvas.width = Math.min(480, Math.max(160, Math.round(innerWidth / 3)));
      canvas.height = Math.min(320, Math.max(160, Math.round(innerHeight / 3)));
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    function draw() {
      if (document.hidden || motion.matches || lost) return;
      time += .05;
      gl.uniform1f(clock, time); gl.uniform1f(mode, theme === 'dark' ? 1 : 0);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    }
    function schedule() {
      clearInterval(timer); timer = null;
      if (!document.hidden && !motion.matches && !lost) { draw(); timer = setInterval(draw, 50); }
    }
    canvas.addEventListener('webglcontextlost', () => { lost = true; clearInterval(timer); canvas.hidden = true; });
    document.addEventListener('visibilitychange', schedule);
    motion.addEventListener('change', schedule);
    window.addEventListener('resize', resize, { passive: true });
    window.addEventListener('pagehide', () => { clearInterval(timer); timer = null; });
    window.addEventListener('pageshow', schedule);
    resize(); schedule();
  });
})();
