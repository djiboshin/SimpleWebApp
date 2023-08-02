<script>
  import * as d3 from 'd3';
  import { onMount } from 'svelte';

  $: data = [];

  async function loadData() {
    const response = await fetch('http://localhost:8000/f')
    data = await response.json()
  }

  onMount(async () => {
    await loadData()
  })
  
</script>

<main>
  <div>{JSON.stringify(data)}</div>
</main>

<style>
  
</style>
