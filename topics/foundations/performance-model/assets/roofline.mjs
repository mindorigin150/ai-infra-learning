function render({ model, el }) {
  el.innerHTML = `<section class="infra-widget">
    <h3>Explore the Roofline model</h3>
    <p class="model-note">Illustrative parameters, not measured hardware. The curve is an upper bound, not a runtime prediction.</p>
    <div class="controls"></div>
    <div class="summary" aria-live="polite"></div>
    <svg viewBox="0 0 700 380" role="img" aria-label="Roofline upper bound versus arithmetic intensity"></svg>
    <div class="legend"><span class="compute">Compute ceiling</span><span class="memory">Bandwidth ceiling</span><span>Combined bound</span></div>
  </section>`;
  const controls = el.querySelector('.controls');
  const chart = el.querySelector('svg');
  const summary = el.querySelector('.summary');
  const settings = [
    { key: 'intensity', label: 'Arithmetic intensity', unit: 'FLOP/byte', min: -2, max: 3 },
    { key: 'bandwidth', label: 'Memory bandwidth', unit: 'GB/s', min: 0, max: 4 },
    { key: 'peak', label: 'Compute peak', unit: 'GFLOP/s', min: 0, max: 5 },
  ];
  const listeners = [];
  for (const setting of settings) {
    const label = document.createElement('label');
    const title = document.createElement('span');
    title.textContent = setting.label;
    const input = document.createElement('input');
    input.type = 'range';
    input.min = setting.min;
    input.max = setting.max;
    input.step = 0.1;
    input.value = Math.log10(model.get(setting.key));
    input.setAttribute('aria-label', setting.label);
    const output = document.createElement('output');
    const update = () => {
      const value = 10 ** Number(input.value);
      model.set(setting.key, value);
      output.value = `${value.toLocaleString('en-US', { maximumSignificantDigits: 3 })} ${setting.unit}`;
      input.setAttribute('aria-valuetext', output.value);
      draw();
    };
    input.addEventListener('input', update);
    listeners.push([input, update]);
    label.append(title, output, input);
    controls.append(label);
    output.value = `${model.get(setting.key).toLocaleString('en-US', { maximumSignificantDigits: 3 })} ${setting.unit}`;
    input.setAttribute('aria-valuetext', output.value);
  }

  function draw() {
    const intensity = model.get('intensity');
    const bandwidth = model.get('bandwidth');
    const peak = model.get('peak');
    const bound = Math.min(peak, bandwidth * intensity);
    const ridge = peak / bandwidth;
    const mode = Math.abs(intensity - ridge) / ridge < 1e-9
      ? 'At the ridge (model)'
      : intensity < ridge ? 'Memory-bound (model)' : 'Compute-bound (model)';
    summary.textContent = `${mode} · bound ${bound.toLocaleString('en-US', { maximumSignificantDigits: 3 })} GFLOP/s · ridge ${ridge.toLocaleString('en-US', { maximumSignificantDigits: 3 })} FLOP/byte`;
    const left = 76, right = 675, top = 28, bottom = 310;
    const yMaxLog = Math.ceil(Math.log10(peak * 1.5));
    const yMinLog = Math.min(yMaxLog - 4, Math.floor(Math.log10(bandwidth * 0.01)));
    const x = (value) => left + (Math.log10(value) + 2) / 5 * (right - left);
    const y = (value) => bottom - (Math.log10(value) - yMinLog) / (yMaxLog - yMinLog) * (bottom - top);
    let grid = '';
    for (let power = -2; power <= 3; power++) {
      const px = x(10 ** power);
      grid += `<line class="grid-line" x1="${px}" y1="${top}" x2="${px}" y2="${bottom}"/><text x="${px}" y="${bottom + 23}" text-anchor="middle">${10 ** power}</text>`;
    }
    for (let power = yMinLog; power <= yMaxLog; power++) {
      const py = y(10 ** power);
      grid += `<line class="grid-line" x1="${left}" y1="${py}" x2="${right}" y2="${py}"/><text x="${left - 10}" y="${py + 4}" text-anchor="end">1e${power}</text>`;
    }
    const points = Array.from({ length: 101 }, (_, index) => {
      const ai = 10 ** (-2 + index / 20);
      return `${x(ai)},${y(Math.min(peak, bandwidth * ai))}`;
    }).join(' ');
    // Clip the bandwidth ceiling geometrically; it can exceed the compute axis range.
    const memoryEnd = Math.min(1000, 10 ** yMaxLog / bandwidth);
    const memoryLine = memoryEnd >= 0.01
      ? `<line class="memory-line" x1="${left}" y1="${y(bandwidth * 0.01)}" x2="${x(memoryEnd)}" y2="${y(bandwidth * memoryEnd)}"/>`
      : '';
    chart.innerHTML = `${grid}
      <line class="axis" x1="${left}" y1="${bottom}" x2="${right}" y2="${bottom}"/>
      <line class="axis" x1="${left}" y1="${top}" x2="${left}" y2="${bottom}"/>
      <line class="compute-line" x1="${left}" y1="${y(peak)}" x2="${right}" y2="${y(peak)}"/>
      ${memoryLine}
      <polyline class="bound-line" points="${points}"/>
      <circle class="workload" cx="${x(intensity)}" cy="${y(bound)}" r="6"/>
      <text x="${(left + right) / 2}" y="365" text-anchor="middle">Arithmetic intensity (FLOP/byte, log scale)</text>
      <text transform="translate(18 170) rotate(-90)" text-anchor="middle">Performance bound (GFLOP/s, log scale)</text>`;
    chart.setAttribute('aria-label', `${mode}; upper bound ${bound} GFLOP/s at intensity ${intensity} FLOP/byte`);
  }
  draw();
  return () => {
    for (const [input, listener] of listeners) input.removeEventListener('input', listener);
    el.replaceChildren();
  };
}

export default { render };
