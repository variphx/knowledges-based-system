<script>
  // ...existing code...
</script>

<div class="container">
  <div class="sidebar">
    <h2>Problems</h2>
    <a class="nav-link" href="/">Home</a>
    <a class="nav-link" href="/about">About</a>
    <a class="nav-link" href="/contact">Contact</a>
  </div>
  <div class="content">
    <div class="header">
      <h1>Header</h1>
    </div>
    <div class="main">
      <!-- ...existing code... -->
      <slot></slot>
      <!-- ...existing code... -->
    </div>
  </div>
</div>

<style>
  .container {
    display: flex;
    height: 100vh;
    overflow: hidden;
  }

  .sidebar {
    width: 250px;
    background-color: #2c3e50;
    color: white;
    display: flex;
    flex-direction: column;
    padding: 20px;
  }

  .header {
    height: 60px;
    background-color: #34495e;
    color: white;
    display: flex;
    align-items: center;
    padding: 0 20px;
  }

  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .main {
    flex: 1;
    overflow: auto;
    padding: 20px;
  }

  .nav-link {
    color: white;
    text-decoration: none;
    margin: 10px 0;
  }

  .nav-link:hover {
    text-decoration: underline;
  }
</style>
