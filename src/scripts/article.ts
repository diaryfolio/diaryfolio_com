const revealSvg = (svg: SVGSVGElement) => {
  svg.style.removeProperty('opacity');
};

const findDrawableGeometry = (svg: SVGSVGElement) =>
  Array.from(svg.querySelectorAll<SVGGeometryElement>('path, line, polyline, polygon, rect, circle, ellipse'))
    .filter((element) => {
      if (element.closest('defs, marker')) return false;

      const style = window.getComputedStyle(element);
      const hasVisibleStroke = style.stroke !== 'none'
        && Number.parseFloat(style.strokeWidth) > 0
        && Number.parseFloat(style.strokeOpacity) > 0;
      const hasNoFill = style.fill === 'none' || Number.parseFloat(style.fillOpacity) === 0;

      return hasVisibleStroke && hasNoFill;
    })
    .slice(0, 80);

const animateMermaidDiagrams = async (diagrams: HTMLElement[]) => {
  const svgs = diagrams
    .map((diagram) => diagram.querySelector<SVGSVGElement>(':scope > svg'))
    .filter((svg): svg is SVGSVGElement => svg !== null);

  if (svgs.length === 0 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  svgs.forEach((svg) => {
    svg.style.opacity = '0';
  });

  try {
    const { animate, inView, stagger } = await import('motion');

    svgs.forEach((svg) => {
      inView(svg, () => {
        const animations = [
          animate(svg, { opacity: [0, 1] }, { duration: 0.25, ease: 'easeOut' })
        ];
        const drawableGeometry = findDrawableGeometry(svg);

        if (drawableGeometry.length > 0) {
          animations.push(animate(
            drawableGeometry,
            { opacity: [0.25, 1], pathLength: [0, 1] },
            { delay: stagger(0.015), duration: 0.7, ease: 'easeInOut' }
          ));
        }

        Promise.allSettled(animations.map((animation) => animation.finished))
          .then(() => revealSvg(svg));
      }, { amount: 0.2 });
    });
  } catch (error) {
    svgs.forEach(revealSvg);
    console.error('Mermaid diagram animation could not be prepared.', error);
  }
};

const revealInlineSvg = (figure: HTMLElement) => {
  figure.querySelectorAll<SVGElement>('[data-svg-step], [data-svg-link]').forEach((element) => {
    element.style.removeProperty('opacity');
    element.style.removeProperty('transform');
    element.style.removeProperty('stroke-dasharray');
    element.style.removeProperty('stroke-dashoffset');
  });
};

const playInlineSvg = (
  figure: HTMLElement,
  animate: typeof import('motion').animate
) => {
  const steps = Array.from(figure.querySelectorAll<SVGElement>('[data-svg-step]'));
  const links = Array.from(figure.querySelectorAll<SVGGeometryElement>('[data-svg-link]'));
  const replay = figure.querySelector<HTMLButtonElement>('[data-svg-replay]');

  replay?.setAttribute('disabled', '');
  [...steps, ...links].forEach((element) => {
    element.style.opacity = '0';
  });

  const animations = [
    ...steps.map((step, index) => animate(
      step,
      { opacity: [0, 1], transform: ['translateY(10px)', 'translateY(0)'] },
      { delay: index * 0.2, duration: 0.42, ease: 'easeOut' }
    )),
    ...links.map((link, index) => animate(
      link,
      { opacity: [0, 1], pathLength: [0, 1] },
      { delay: 0.12 + index * 0.2, duration: 0.38, ease: 'easeInOut' }
    ))
  ];

  Promise.allSettled(animations.map((animation) => animation.finished))
    .then(() => {
      revealInlineSvg(figure);
      replay?.removeAttribute('disabled');
    });
};

const animateInlineSvgs = async () => {
  const figures = Array.from(document.querySelectorAll<HTMLElement>('.article-svg-figure[data-animate-svg]'));

  if (figures.length === 0) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    figures.forEach((figure) => {
      figure.querySelector<HTMLButtonElement>('[data-svg-replay]')?.setAttribute('hidden', '');
    });
    return;
  }

  figures.forEach((figure) => {
    figure.querySelectorAll<SVGElement>('[data-svg-step], [data-svg-link]').forEach((element) => {
      element.style.opacity = '0';
    });
  });

  try {
    const { animate, inView } = await import('motion');

    figures.forEach((figure) => {
      const replay = figure.querySelector<HTMLButtonElement>('[data-svg-replay]');
      replay?.removeAttribute('hidden');
      replay?.addEventListener('click', () => playInlineSvg(figure, animate));

      inView(figure, () => {
        playInlineSvg(figure, animate);
      }, { amount: 0.2 });
    });
  } catch (error) {
    figures.forEach((figure) => {
      revealInlineSvg(figure);
      figure.querySelector<HTMLButtonElement>('[data-svg-replay]')?.setAttribute('hidden', '');
    });
    console.error('Inline SVG animation could not be prepared.', error);
  }
};

const prepareMermaidDiagrams = async () => {
  const diagramBlocks = Array.from(document.querySelectorAll<HTMLElement>('.prose pre'))
    .filter((pre) => pre.dataset.language === 'mermaid' || Boolean(pre.querySelector(':scope > code.language-mermaid')));

  if (diagramBlocks.length === 0) return;

  const diagrams = diagramBlocks.map((pre) => {
    const source = (pre.textContent ?? '').trim();
    const figure = document.createElement('figure');
    const diagram = document.createElement('div');

    figure.className = 'mermaid-figure is-loading';
    diagram.className = 'mermaid-diagram';
    diagram.dataset.source = source;
    diagram.setAttribute('aria-busy', 'true');
    diagram.textContent = source;
    pre.replaceWith(figure);
    figure.append(diagram);

    return { diagram, figure, source };
  });

  const { default: mermaid } = await import('mermaid');
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'strict',
    theme: 'base',
    themeVariables: {
      background: '#ffffff',
      primaryColor: '#e5f2f4',
      primaryBorderColor: '#087286',
      primaryTextColor: '#18232c',
      secondaryColor: '#f6ebe7',
      secondaryBorderColor: '#b44a35',
      secondaryTextColor: '#18232c',
      tertiaryColor: '#edf2f4',
      tertiaryBorderColor: '#5e6c77',
      tertiaryTextColor: '#18232c',
      lineColor: '#5e6c77',
      textColor: '#18232c',
      fontFamily: 'Inter, ui-sans-serif, system-ui, sans-serif',
      fontSize: '15px'
    },
    flowchart: {
      htmlLabels: false,
      useMaxWidth: true
    }
  });

  const renderedDiagrams: HTMLElement[] = [];

  for (const { diagram, figure, source } of diagrams) {
    try {
      await mermaid.run({ nodes: [diagram] });
      diagram.setAttribute('aria-busy', 'false');
      figure.classList.remove('is-loading');
      renderedDiagrams.push(diagram);
    } catch (error) {
      const fallback = document.createElement('pre');
      const code = document.createElement('code');

      fallback.className = 'mermaid-fallback';
      code.textContent = source;
      fallback.append(code);
      diagram.replaceWith(fallback);
      figure.classList.remove('is-loading');
      console.error('Mermaid diagram could not be rendered.', error);
    }
  }

  await animateMermaidDiagrams(renderedDiagrams);
};

const enhanceCodeBlocks = () => {
  document.querySelectorAll<HTMLPreElement>('.prose pre').forEach((pre) => {
    if (pre.classList.contains('mermaid-fallback')) return;

    const codeText = (pre.textContent ?? '').trim();
    pre.textContent = codeText;
    const block = document.createElement('div');
    block.className = 'code-block';
    const toolbar = document.createElement('div');
    toolbar.className = 'code-toolbar';
    const label = document.createElement('span');
    label.textContent = 'Snippet';
    const actions = document.createElement('span');
    actions.className = 'code-actions';
    const copy = document.createElement('button');
    copy.className = 'code-copy';
    copy.type = 'button';
    copy.textContent = 'Copy';
    copy.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(codeText); copy.textContent = 'Copied'; } catch { copy.textContent = 'Select and copy'; }
      window.setTimeout(() => { copy.textContent = 'Copy'; }, 1400);
    });
    actions.append(copy);
    if (codeText.length > 280 || codeText.split('\n').length > 10) {
      pre.classList.add('code-collapsed');
      const toggle = document.createElement('button');
      toggle.className = 'code-toggle';
      toggle.type = 'button';
      toggle.textContent = 'Expand';
      toggle.addEventListener('click', () => {
        const expanded = pre.classList.toggle('code-expanded');
        toggle.textContent = expanded ? 'Collapse' : 'Expand';
      });
      actions.prepend(toggle);
    }
    toolbar.append(label, actions);
    pre.replaceWith(block);
    block.append(toolbar, pre);
  });
};

export const enhanceArticle = async () => {
  await prepareMermaidDiagrams();
  await animateInlineSvgs();
  enhanceCodeBlocks();
};
