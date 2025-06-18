<script setup lang="ts">
const isMounted = useMountedCheck();
</script>
<template>
  <div
    v-if="isMounted"
    class="flex flex-col w-full items-center"
  >
    <div
      class="fixed inset-0 bg-gradient-to-br from-neutral-100 to-neutral-200 dark:from-neutral-900 dark:to-neutral-800 transition"
    />
    <div class="relative flex flex-col items-center justify-stretch min-h-screen gap-6 px-6 w-full">
      <Header />
      <Container class="grow">
        <Hype />
      </Container>
      <Container>
        <Result />
      </Container>
      <div class="h-4" />
    </div>
    <Footer />
  </div>
</template>
