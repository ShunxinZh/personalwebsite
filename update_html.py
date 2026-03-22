import sys

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()
        
    replacements = [
        ('PhD Candidate · Molecular Machenism&nbsp;Evolution', 'Graduate Student · Biological Sciences'),
        ('src="https://lh3.googleusercontent.com/aida-public/AB6AXuBfMMvIlZuaPZ4COtMBX5yOBzMdBjnSNIg9XPfSlkeu_sm9CwSNIMekbnv_6fwsUDcoGoSj08s4ITEQ01RjYuYxSL6JrohjIZASUDaNMhxboumGFLCa-gIHeWwg2Mf-Dk_XQrbUoPNtBgxxmLpCjqp6I4eM2-2pqK-tsC12uifBsJmUPgzqriaVeXWl9gzbunIPBK8nHQc1Z3ZslRhSgzkYTlikFWDPIoQf6NHklMe1oLY-jEc6f1OncWDTk5-ETqKQ6jo37_QA1Oo"', 'src="1740262331764.jpg"'),
        ('alt="Abstract microscopic visualization of molecular structures"', 'alt="Headshot of Shunxin Zhou"'),
        ('data-alt="Abstract microscopic visualization of molecular structures"', 'data-alt="Headshot of Shunxin Zhou"'),
        ('Currently a PhD Candidate specializing in Evolutionary Systems Biology, my work sits at the intersection of molecular laboratory techniques and computational analysis. I am passionate about uncovering the elegant rules that govern how life adapts at its most fundamental level.', 'Currently a Graduate Student in Biological Sciences at Purdue University. My research focuses on the molecular mechanisms of plant-microbe interactions and evolutionary trajectories, combining molecular laboratory techniques with computational analysis.'),
        ('Before my doctoral studies, I completed my Masters at the University of Zurich, focusing on the biochemical characterization of extremophile proteins. When not in the lab or at my terminal, I contribute to open-source biological data visualization tools.', 'Before my doctoral studies, I completed my M.S. in Agronomy and Seed Industry at the Chinese Academy of Agricultural Sciences, and my B.Sc. in Seed Science and Engineering at Northeast Agricultural University. I am passionate about uncovering the elegant rules that govern how life adapts at its most fundamental level.'),
        ('Journal of Evolution', 'Plants (Basel)'),
        ('<span class="text-xs text-outline font-label">2024</span>', '<span class="text-xs text-outline font-label">2021</span>'),
        ('Structural Determinants of Enzyme Plasticity in Ancestral Metabolic Pathways', 'Characteristics and research progress of legume nodule senescence'),
        ('Zhou, S., &amp; Miller, A. This study utilizes high-resolution crystallography to demonstrate how conformational entropy drives early functional divergence.', 'Shunxin Zhou, Chanjuan Zhang, Yi Huang, Haifeng Chen, Songli Yuan, Xinan Zhou. Plants (Basel). 2021;10(6):1103.'),
        ('Nature Molecular Biology', 'Frontiers in Microbiology'),
        ('<span class="text-xs text-outline font-label">2023</span>', '<span class="text-xs text-outline font-label">2021</span>'),
        ('The Evolutionary Significance of Non-Canonical DNA Structure Stability', 'Identification of the important genes of Bradyrhizobium diazoefficiens 113-2'),
        ('Zhou, S., et al. Exploring the constraints imposed by G-quadruplex dynamics on the evolutionary rates of thermophilic microorganisms.', 'Songli Yuan, Shunxin Zhou, et al. Involved in soybean nodule development and senescence.'),
        ('Proteomics Quarterly', 'Journal of Experimental Botany'),
        ('<span class="text-xs text-outline font-label">2022</span>', '<span class="text-xs text-outline font-label">2023</span>'),
        ('Predictive Modeling of Proteomic Adaptation Under Extreme Stress', 'The Bax inhibitor GmBI-1α interacts with a Nod factor receptor'),
        ('Lee, H. &amp; Zhou, S. Computational framework for assessing the robustness of cellular proteomes in hyper-saline environments.', 'Songli Yuan, et al. Plays a dual role in the legume–rhizobia symbiosis.'),
        ("""<div>
<h4 class="font-label text-xs uppercase tracking-widest text-outline mb-4">Fellowships</h4>
<ul class="font-body text-sm space-y-4">
<li>National Science Foundation Graduate Fellow <br> <span class="text-outline">2022 – Present</span></li>
<li>EMBO Short-Term Fellowship <br> <span class="text-outline">2021</span></li>
</ul>
</div>""", """<div>
<h4 class="font-label text-xs uppercase tracking-widest text-outline mb-4">Education</h4>
<ul class="font-body text-sm space-y-4">
<li>M.S., Agronomy & Seed Industry <br> <span class="text-outline">CAAS, Beijing (2019-2022)</span></li>
<li>B.Sc., Seed Science & Engineering <br> <span class="text-outline">NEAU, Harbin (2015-2019)</span></li>
</ul>
</div>"""),
        ("""<div>
<h4 class="font-label text-xs uppercase tracking-widest text-outline mb-4">Teaching</h4>
<ul class="font-body text-sm space-y-4">
<li>Lead TA: Molecular Phylogenetics <br> <span class="text-outline">Fall 2023</span></li>
<li>Workshop Instructor: R for Biologists <br> <span class="text-outline">Spring 2022</span></li>
</ul>
</div>""", """<div>
<h4 class="font-label text-xs uppercase tracking-widest text-outline mb-4">Research Experience</h4>
<ul class="font-body text-sm space-y-4">
<li>National Major Transgenic Project <br> <span class="text-outline">2021-2022</span></li>
<li>Natural Science Foundation <br> <span class="text-outline">2019-2022</span></li>
</ul>
</div>"""),
        ('shunxin.zhou@university.edu', 'zhou1453@purdue.edu')
    ]

    for old, new in replacements:
        if old not in text:
            print(f"Warning: Could not find string to replace:\n{old[:50]}...")
        text = text.replace(old, new)
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replacements complete.")

if __name__ == '__main__':
    update_html()
