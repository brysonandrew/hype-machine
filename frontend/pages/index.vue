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
    <div class="relative flex flex-col justify-stretch min-h-screen gap-6 px-6">
      <Header />
      <Container class="grow">
        <div class="flex flex-col items-end justify-center gap-12 py-4 grow">
          <Mode/>
          <Hype />
        </div>
      </Container>
      <Container>
        <Result />
      </Container>
      <div class="h-4" />
    </div>
    <Footer />
  </div>
</template>
