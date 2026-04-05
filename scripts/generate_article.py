#!/usr/bin/env python3
"""
=============================================================
Générateur d'articles pour Adaptogènes & Santé
=============================================================

Ce script génère un template HTML complet pour un nouvel article
d'adaptogène, avec toute la structure SEO (meta tags, JSON-LD,
Open Graph) et les placeholders pour le contenu et les produits.

Usage:
    python generate_article.py "Nom de l'adaptogène" "mot-clé-slug"

Exemple:
    python generate_article.py "Cordyceps" "cordyceps"
    python generate_article.py "Lion's Mane" "lions-mane"
    python generate_article.py "Tulsi (Basilic Sacré)" "tulsi"

Le fichier HTML sera créé dans ../articles/{slug}.html
"""

import sys
import os
from datetime import date


def generate_article(name: str, slug: str):
    """Génère un fichier HTML d'article complet pour un adaptogène."""

    today = date.today().isoformat()
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'articles')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'{slug}.html')

    if os.path.exists(output_path):
        print(f"⚠️  Le fichier {output_path} existe déjà. Utilisez --force pour écraser.")
        if '--force' not in sys.argv:
            sys.exit(1)

    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} : Bienfaits, Dosage et Meilleurs Compléments {date.today().year}</title>
  <meta name="description" content="Guide complet sur {name} : bienfaits prouvés scientifiquement, dosage optimal et comparatif des meilleurs compléments en {date.today().year}.">
  <meta name="keywords" content="{slug}, adaptogène, bien-être, santé naturelle, complément alimentaire">
  <link rel="canonical" href="https://adaptogenes-sante.github.io/articles/{slug}.html">
  <meta property="og:title" content="{name} : Bienfaits, Dosage et Meilleurs Compléments {date.today().year}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="fr_FR">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{name} : Bienfaits, Dosage et Meilleurs Compléments {date.today().year}","author":{{"@type":"Organization","name":"Adaptogènes & Santé"}},"datePublished":"{today}","dateModified":"{today}"}}
  </script>
</head>
<body>
  <nav class="nav" id="nav"><div class="nav-inner"><a href="../index.html" class="nav-logo"><span class="logo-icon">🌿</span> Adaptogènes & Santé</a><ul class="nav-links" id="navLinks"><li><a href="../index.html#adaptogens">Les Adaptogènes</a></li><li><a href="../index.html#articles">Nos Guides</a></li><li><a href="ashwagandha.html">Ashwagandha</a></li><li><a href="rhodiola.html">Rhodiola</a></li><li><a href="maca.html">Maca</a></li></ul><button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button></div></nav>

  <header class="article-hero"><div class="article-hero-inner">
    <div class="article-breadcrumb"><a href="../index.html">Accueil</a> <span>›</span> <a href="../index.html#articles">Guides</a> <span>›</span> <span>{name}</span></div>
    <h1>{name} : Bienfaits, Dosage et Meilleurs Compléments {date.today().year}</h1>
    <div class="article-meta"><span>📅 {today}</span><span>⏱️ X min de lecture</span><span>🏷️ Catégorie</span></div>
  </div></header>

  <main class="article-content">

    <!-- TODO: Ajouter une image -->
    <!-- <img src="../images/{slug}.png" alt="{name}" style="border-radius:var(--radius-lg);margin-bottom:var(--space-2xl);width:100%;"> -->

    <p>
      <!-- TODO: Introduction de l'article -->
      Introduction sur <strong>{name}</strong> — son origine, son histoire et pourquoi il/elle est considéré(e) comme un adaptogène puissant.
    </p>

    <div class="info-box"><h4>💡 En bref</h4><p><!-- TODO: Résumé rapide des bienfaits clés --></p></div>

    <h2>Qu'est-ce que {name} ?</h2>
    <p><!-- TODO: Description botanique, origine, composés actifs --></p>

    <h2>Bienfaits prouvés</h2>

    <h3>1. Premier bienfait</h3>
    <p><!-- TODO: Description avec études scientifiques --></p>

    <h3>2. Deuxième bienfait</h3>
    <p><!-- TODO: Description avec études scientifiques --></p>

    <h3>3. Troisième bienfait</h3>
    <p><!-- TODO: Description avec études scientifiques --></p>

    <h2>Dosage recommandé</h2>
    <div class="info-box"><h4>📋 Dosage</h4><p><!-- TODO: Dosage optimal avec détails --></p></div>

    <h2>Top 5 des meilleurs compléments de {name} {date.today().year}</h2>
    <div class="product-table-wrapper"><table class="product-table">
      <thead><tr><th>Produit</th><th>Type</th><th>Dosage</th><th>Note</th><th>Prix</th><th>Lien</th></tr></thead>
      <tbody>
        <tr class="best-pick">
          <td class="product-name"><!-- TODO: Nom du produit --></td>
          <td><!-- Type --></td>
          <td><!-- Dosage --></td>
          <td class="product-rating">⭐ X.X/5</td>
          <td>XX,XX€</td>
          <td><a href="https://www.amazon.fr/dp/ASIN?tag=TON-TAG-21" class="btn-table-amazon" target="_blank" rel="noopener sponsored">Voir sur Amazon</a></td>
        </tr>
        <!-- TODO: Ajouter 4 autres produits -->
      </tbody>
    </table></div>

    <div class="affiliate-disclaimer"><strong>⚠️ Transparence :</strong> Liens affiliés. Commission sans surcoût pour vous.</div>

    <h2>Précautions</h2>
    <ul>
      <li><!-- TODO: Effet secondaire 1 --></li>
      <li><!-- TODO: Effet secondaire 2 --></li>
    </ul>

    <h2>Conclusion</h2>
    <p><!-- TODO: Résumé et recommandation finale --></p>
  </main>

  <section class="related-articles"><div class="related-articles-inner"><h2>Articles connexes</h2><div class="related-grid">
    <article class="article-card"><div class="article-card-image"><img src="../images/ashwagandha.png" alt="Ashwagandha" loading="lazy"><span class="article-card-tag">Anti-stress</span></div><div class="article-card-body"><h3><a href="ashwagandha.html">Ashwagandha</a></h3><p class="article-card-excerpt">Le guide complet.</p><div class="article-card-meta"><a href="ashwagandha.html" class="read-more-link">Lire →</a></div></div></article>
    <article class="article-card"><div class="article-card-image"><img src="../images/rhodiola.png" alt="Rhodiola" loading="lazy"><span class="article-card-tag">Énergie</span></div><div class="article-card-body"><h3><a href="rhodiola.html">Rhodiola</a></h3><p class="article-card-excerpt">Énergie naturelle.</p><div class="article-card-meta"><a href="rhodiola.html" class="read-more-link">Lire →</a></div></div></article>
  </div></div></section>

  <footer class="footer"><div class="footer-inner">
    <div class="footer-brand"><div class="footer-logo">🌿 Adaptogènes & Santé</div><p>Guide de référence sur les adaptogènes.</p></div>
    <div class="footer-col"><h4>Guides</h4><ul><li><a href="ashwagandha.html">Ashwagandha</a></li><li><a href="rhodiola.html">Rhodiola</a></li><li><a href="maca.html">Maca</a></li><li><a href="reishi.html">Reishi</a></li><li><a href="ginseng.html">Ginseng</a></li></ul></div>
    <div class="footer-col"><h4>Info</h4><ul><li><a href="#">À propos</a></li><li><a href="#">Contact</a></li><li><a href="#">Mentions légales</a></li></ul></div>
  </div><div class="footer-bottom"><span>© {date.today().year} Adaptogènes & Santé.</span></div></footer>
  <script src="../js/main.js"></script>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Article créé : {output_path}")
    print(f"📝 Ouvrez le fichier et remplacez les <!-- TODO --> par votre contenu.")
    print(f"🔗 N'oubliez pas de mettre à jour le sitemap.xml et d'ajouter le lien sur index.html")

    # Update sitemap
    sitemap_path = os.path.join(os.path.dirname(__file__), '..', 'sitemap.xml')
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_entry = f"""  <url>
    <loc>https://adaptogenes-sante.github.io/articles/{slug}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""

        content = content.replace('</urlset>', new_entry)

        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"🗺️  Sitemap mis à jour automatiquement.")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python generate_article.py \"Nom\" \"slug\"")
        print("Exemple: python generate_article.py \"Cordyceps\" \"cordyceps\"")
        sys.exit(1)

    name = sys.argv[1]
    slug = sys.argv[2]
    generate_article(name, slug)
